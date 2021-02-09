import numpy as np
import tensorflow as tf
import os, argparse
import cv2
import json
import shutil
from .data import process_image_file

from collections import defaultdict

def score_prediction(softmax, step_size):
    vals = np.arange(3) * step_size + (step_size / 2.)
    vals = np.expand_dims(vals, axis=0)
    return np.sum(softmax * vals, axis=-1)

class MetaModel:
    def __init__(self, meta_file, ckpt_file):
        self.meta_file = meta_file
        self.ckpt_file = ckpt_file

        self.graph = tf.Graph()
        with self.graph.as_default():
            self.saver = tf.train.import_meta_graph(self.meta_file)
            self.input_tr = self.graph.get_tensor_by_name('input_1:0')
            self.phase_tr = self.graph.get_tensor_by_name('keras_learning_phase:0')
            self.output_tr = self.graph.get_tensor_by_name('MLP/dense_1/MatMul:0')

    def infer(self, image):
        with tf.Session(graph=self.graph) as sess:
            self.saver.restore(sess, self.ckpt_file)

            outputs = defaultdict(list)
            outs = sess.run(self.output_tr,
                            feed_dict={
                                self.input_tr: np.expand_dims(image, axis=0),
                                self.phase_tr: False
                            })
            outputs['logits'].append(outs)

            for k in outputs.keys():
                outputs[k] = np.concatenate(outputs[k], axis=0)

            outputs['softmax'] = np.exp(outputs['logits']) / np.sum(
                np.exp(outputs['logits']), axis=-1, keepdims=True)
            outputs['score'] = score_prediction(outputs['softmax'], 1 / 3.)

        return outputs['score']


class Inference():
    '''
        the args dict should have:
        weightspath: str, metaname : str, ckptname: str
    '''
    def __init__(self, args):
        self.args = args

    def infer(self):
        mapping = {'normal': 0, 'pneumonia': 1, 'COVID-19': 2}
        inv_mapping = {0: 'normal', 1: 'pneumonia', 2: 'COVID-19'}
        args = self.args
        args.imagepath = self.args.inputdir + '/' + self.args.imagefile
        
        # sess = tf.Session()
        tf.reset_default_graph()
        with tf.Session() as sess:
            tf.get_default_graph()
            saver = tf.train.import_meta_graph(
                os.path.join(args.weightspath, args.metaname))
            saver.restore(sess, os.path.join(args.weightspath, args.ckptname))

            graph = tf.get_default_graph()

            image_tensor = graph.get_tensor_by_name(args.in_tensorname)
            pred_tensor = graph.get_tensor_by_name(args.out_tensorname)

            x = process_image_file(args.imagepath, args.top_percent,
                                   args.input_size)
            x = x.astype('float32') / 255.0
            pred = sess.run(
                pred_tensor,
                feed_dict={image_tensor: np.expand_dims(x, axis=0)})

        output_dict = {
            '**DISCLAIMER**':
            'Do not use this prediction for self-diagnosis. You should check with your local authorities for the latest advice on seeking medical assistance.',
            "prediction": inv_mapping[pred.argmax(axis=1)[0]],
            "Normal": str(pred[0][0]),
            "Pneumonia": str(pred[0][1]),
            "COVID-19": str(pred[0][2])
        }

        # if predication is covid positive, run the two other models
        severityScores = None
        if output_dict["prediction"] == 'COVID-19':
            severityScores = self.generate_severity_data(args.imagepath)
        
        self.generate_output_files(output_dict, severityScores)

        return output_dict
        
    def generate_severity_data(self, imagePath):
        models = ['/usr/local/lib/covidnet/COVIDNet-SEV-GEO','/usr/local/lib/covidnet/COVIDNet-SEV-OPC']
        res = {}
        for modelName in models:
            args = {
              "weightspath":'/usr/local/lib/covidnet/COVIDNet-SEV-GEO',
              "metaname":"model.meta",
              "ckptname":"model",
              "input_size":480,
              "top_percent":0.08
            }

            x = process_image_file(imagePath, args['top_percent'], args['input_size'])
            x = x.astype('float32') / 255.0

            model = MetaModel(os.path.join(args['weightspath'], args['metaname']),
                              os.path.join(args['weightspath'], args['ckptname']))
            output = model.infer(x)

            if modelName.endswith('COVIDNet-SEV-GEO'):
                res["Geographic severity"] = str(int(round(output[0]*100)))
                res['Geographic extent score'] = str(round(output[0] * 8, 1))
                res['GeoInfo'] = "For each lung: 0 = no involvement; 1 = <25%; 2 = 25-50%; 3 = 50-75%; 4 = >75% involvement."
            elif modelName.endswith('COVIDNet-SEV-OPC'):
                res["Opacity severity"] = str(int(round(output[0]*100)))
                res['Opacity extent score'] = str(round(output[0] * 6, 1))
                res['OpcInfo'] = 'For each lung: 0 = no opacity; 1 = ground glass opacity; 2 =consolidation; 3 = white-out.'
        return res

    def generate_output_files(self, classification_data, severityScores):
        # remove this line to display model names mapped in dict
        self.args.modelused = 'default'

        # creates the output directory if not exists
        if not os.path.exists(self.args.outputdir):
            os.makedirs(self.args.outputdir)

        print("Creating prediction.json in {}...".format(self.args.outputdir))
        with open('{}/prediction-{}.json'.format(self.args.outputdir, self.args.modelused), 'w') as f:
            json.dump(classification_data, f, indent=4)
        
        print("Copying over the input image to: {}...".format(self.args.outputdir))
        shutil.copy(self.args.inputdir + '/' + self.args.imagefile,self.args.outputdir)

        # Not covid positive
        if severityScores is None:
          return
        
        print("Creating severity.json in {}...".format(self.args.outputdir))
        with open('{}/severity.json'.format(self.args.outputdir), 'w') as f:
            json.dump(severityScores, f, indent=4)
    


    
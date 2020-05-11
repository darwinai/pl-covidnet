import numpy as np
import tensorflow as tf
import os, argparse
import cv2
import json
import shutil 


class Inference():
    '''
        the args dict should have:
        weightspath: str, metaname : str, ckptname: str
    '''
    def __init__(self, args):
        self.args = args

    def infer(self, options):
        mapping = {'normal': 0, 'pneumonia': 1, 'COVID-19': 2}
        inv_mapping = {0: 'normal', 1: 'pneumonia', 2: 'COVID-19'}
        args = self.args
        args.imagepath = os.getcwd()+'/'+options.inputdir+'/'+options.imagefile

        # sess = tf.Session()
        tf.reset_default_graph()
        with tf.Session() as sess:
            tf.get_default_graph()
            saver = tf.train.import_meta_graph(os.path.join(args.weightspath, args.metaname))
            saver.restore(sess, os.path.join(args.weightspath, args.ckptname))

            graph = tf.get_default_graph()

            image_tensor = graph.get_tensor_by_name("input_1:0")
            pred_tensor = graph.get_tensor_by_name("dense_3/Softmax:0")

            x = cv2.imread(args.imagepath)
            h, w, c = x.shape
            x = x[int(h/6):, :]
            x = cv2.resize(x, (224, 224))
            x = x.astype('float32') / 255.0
            pred = sess.run(pred_tensor, feed_dict={image_tensor: np.expand_dims(x, axis=0)})
        
        output_dict = {
            '**DISCLAIMER**':'Do not use this prediction for self-diagnosis. You should check with your local authorities for the latest advice on seeking medical assistance.',
            "prediction":inv_mapping[pred.argmax(axis=1)[0]],
            "Normal":str(pred[0][0]),
            "Pneumonia":str(pred[0][1]),
            "COVID-19":str(pred[0][2])
        }

        self.generate_output_files(options, output_dict)

        return output_dict
        
    
    def generate_output_files(self,options,data):
        # creates the output directory if not exists
        if not os.path.exists(options.outputdir):
            os.makedirs(options.outputdir)
        
        print("Creating prediction.json...")
        with open('{}/prediction.json'.format(options.outputdir), 'w') as f:
            json.dump(data, f, indent=4)
        
        print("Creating prediction.txt...")
        with open('{}/prediction.txt'.format(options.outputdir), 'w') as f:
            f.write('Prediction: {}\n'.format(data['prediction']))
            f.write('Confidence\n')
            f.write('Normal: {}, Pneumonia: {}, COVID-19: {}\n'.format(data['Normal'], data['Pneumonia'], data['COVID-19']))
            f.write('**DISCLAIMER**\n')
            f.write('Do not use this prediction for self-diagnosis. You should check with your local authorities for the latest advice on seeking medical assistance.')

        print("Copying over the input image...")
        shutil.copy(options.inputdir+'/'+options.imagefile, options.outputdir)
import os, argparse
from inference import Inference

for (dirpath, dirnames, filenames) in os.walk("test_images"):
    count = {
        "normal": 0,
        "pneumonia": 0,
        "COVID-19": 0
    }
    for file in filenames:
        parser = argparse.ArgumentParser(description='COVID-Net Inference')
        parser.add_argument('--weightspath', default=os.getcwd()+'/../../COVID-Net/models/COVIDNet-CXR-Large', type=str, help='Path to output folder')
        parser.add_argument('--metaname', default='model.meta', type=str, help='Name of ckpt meta file')
        parser.add_argument('--ckptname', default='model-8485', type=str, help='Name of model ckpts')
        parser.add_argument('--outputdir', default='output', type=str, help='Name of model ckpts')

        args = parser.parse_args()
        app = Inference(args)
        print('Processing {}'.format(file))
        parser = argparse.ArgumentParser(description='COVID-Net Inference')
        parser.add_argument('--inputdir', default='test_images', type=str, help='Path to output folder')
        parser.add_argument('--imagefile', default=file, type=str, help='Path to output folder')
        parser.add_argument('--outputdir', default='outputdir', type=str, help='Path to output folder')


        args = parser.parse_args()

        result = app.infer(args)
        count[result['prediction']] += 1

    for pred_type in count:
        print("{} : {}".format(pred_type, count[pred_type])) 
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
        parser.add_argument('-p', '--weightspath', 
                    dest         = 'weightspath', 
                    type         = str, 
                    help         = 'Path to output folder',
                    default      = os.getcwd()+'/models/COVIDNet-CXR3-B')
        parser.add_argument('--metaname', 
                    dest         = 'metaname', 
                    type         = str, 
                    help         = 'Name of ckpt meta file',
                    default      = 'model.meta')
        parser.add_argument('--ckptname', 
                    dest         = 'ckptname', 
                    type         = str, 
                    help         = 'Name of model ckpts',
                    default      = 'model-1014')
        parser.add_argument('--imagefile', 
                    dest         = 'imagefile', 
                    type         = str, 
                    default      = file,
                    help         = 'Name of image file to infer from')
        parser.add_argument('--in_tensorname', 
                    dest         = 'in_tensorname', 
                    type         = str, 
                    help         = 'Name of input tensor to graph',
                    default      = 'input_1:0')
        parser.add_argument('--out_tensorname', 
                    dest         = 'out_tensorname', 
                    type         = str, 
                    help         = 'Name of output tensor from graph',
                    default      = 'norm_dense_1/Softmax:0')
        parser.add_argument('--input_size', 
                    dest         = 'input_size', 
                    type         = int, 
                    help         = 'Size of input (ex: if 480x480, --input_size 480)',
                    default      = 480)
        parser.add_argument('--top_percent', 
                    dest         = 'top_percent', 
                    type         = float, 
                    help         = 'Percent top crop from top of image',
                    default      = 0.08)
        parser.add_argument('--inputdir', 
                    dest         = 'inputdir', 
                    type         = str, 
                    default      = 'test_images')
        parser.add_argument('--outputdir', 
                    dest         = 'outputdir', 
                    type         = str, 
                    default      = 'output')

        args = parser.parse_args()
        app = Inference(args)
        print('Processing {}'.format(file))

        result = app.infer()
        count[result['prediction']] += 1

    for pred_type in count:
        print("{} : {}".format(pred_type, count[pred_type])) 
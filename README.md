# crop-samples-point
This python script crops boxes of diferent size over a set of images, indicated by samples point in a json file

usage: extract-samples-point.py [-h] -s SIZES [SIZES ...] -t TAGS [TAGS ...]
                                -jf JSONFILES [JSONFILES ...]

optional arguments:
  -h, --help            show this help message and exit
  -s SIZES [SIZES ...]  box size to be cropped around the sample point
  -t TAGS [TAGS ...]    sample point tag to be cropped (see class in .json file)
  -jf JSONFILES [JSONFILES ...]
                        .json file with annotations over the images. We assumes that the set of images are under /imgs folder in actual path


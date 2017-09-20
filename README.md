# crop-samples-point
## This python script crops boxes of different size over a set of images, indicated by samples point in a annotations json file performed with Sloth Labeling

<p align="center">
  <img src="https://user-images.githubusercontent.com/16541529/30553977-487e6142-9c79-11e7-8053-5d155086f298.png" alt="SamplesPoint" width="350px" />
</p>

# Usage 
usage: crop-samples-point.py [-h] -s SIZES [SIZES ...] -t TAGS [TAGS ...] -jf
                             JSONFILES [JSONFILES ...]

Crops images around the sample point with user defined sizes

optional arguments:
  -h, --help            show this help message and exit
  
  -s SIZES [SIZES ...]  Box size to be cropped around the sample point
  
  -t TAGS [TAGS ...]    Sample point tag to be cropped (see class in .json
                        file)
                        
  -jf JSONFILES [JSONFILES ...]
                        .json file with annotations over the images. We
                        assumed that the set of images are under /imgs folder
                        in current path

# Contributing to annotations

If you'd like to provide annotation, you can do so by using [Sloth](http://sloth.readthedocs.org/en/latest/), a versatile tool for various labeling tasks in the context of computer vision research.

https://github.com/cvhciKIT/sloth

# Thanks to:
+ Smerity
This script was inspired on https://github.com/Smerity/right_whale_hunt/blob/master/README.md

+ nilsonholger


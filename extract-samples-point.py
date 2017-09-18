import json
import math
import os
import sys
import argparse
###
from PIL import Image

def ensure_dir(fn):
  d = os.path.dirname(fn)
  if not os.path.exists(d):
    os.makedirs(d)

parser = argparse.ArgumentParser(description='Crop images around the sample point with size indicates')

#parser.add_argument("-fp", dest="filepath", type=str, metavar="PATH",
#                    help="PATH of input images")

parser.add_argument("-s", dest="sizes", type=int,required=True,nargs='+', help="box size to be cropped around the sample point")
parser.add_argument("-t", dest="tags",type=str,required=True,nargs='+', help="sample point tag to be cropped (see class in .json file)")   #eg.: sample-point-sea,sample-point-sky,sample-point-dolphin             
parser.add_argument("-jf", dest="jsonfiles", type=str,required=True, nargs='+', help=".json file with annotations over the images. We assumes that the set of images are under /imgs folder in actual path")

args = parser.parse_args()
# Load the JSON annotations - for each one json file ...
for json_fn in args.jsonfiles:
  annotations = json.loads(open(json_fn).read())
  for data in annotations:
    fn = data['filename'] #for each one img file ...
    # Fix any filenames that start with '../imgs/'
    fn = fn[3:] if fn.startswith('../') else fn
    print 'Processing {}'.format(fn)
    if data['annotations']:
      # We're only interested in the classes of tags
      #for each one class of tag ... 
      for tag in args.tags:
          points = [x for x in data['annotations'] if x['class'] == tag]
          if not points:
            continue
          points = points[0]
          print 'Processing {}'.format(fn)
          
          # TODO check for out of range in the image
          for size in args.sizes:#for each one windows size ...
              yleft =  points['y'] - (size /2) - 1
              xupper =  points['x'] - (size /2) - 1
              yright = points['y'] + (size /2)
              xlower =  points['x'] + (size /2)
                            
              box = map(int, [yleft, xupper, yright, xlower])
              im = Image.open(fn)
              cropped=im.crop(box)

              #make new dir with the name of the tag and the size
              outdir=os.path.dirname(fn) +'/'+ tag + str(size) +'x'+ str(size)
              if not os.path.exists(outdir):
                  os.makedirs(outdir)
              
              #make new file name to save the cropped image
              orginalfn=os.path.basename(fn)             
              croppedfn=os.path.splitext(orginalfn)[0]+'_'+ str(size) +'x'+ str(size) + os.path.splitext(orginalfn)[1]
              outdirfn=outdir+'/'+croppedfn
              
              #save cropped box image in /imgs/tag-sizexsize-folder/original-name-sizexsize.extesion-file
              cropped.save(outdirfn)

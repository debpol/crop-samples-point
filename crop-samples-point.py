import json
import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Crops images around the sample point with user defined sizes')

#parser.add_argument("-fp", dest="filepath", type=str, metavar="PATH",
#                    help="PATH of input images")

parser.add_argument("-s", dest="sizes", type=int,required=True,nargs='+', help="Box size to be cropped around the sample point")
parser.add_argument("-t", dest="tags",type=str,required=True,nargs='+', help="Sample point tag to be cropped (see class in .json file)")   #eg.: sample-point-sea,sample-point-sky,sample-point-dolphin             
parser.add_argument("-jf", dest="jsonfiles", type=str,required=True, nargs='+', help=".json file with annotations over the images. We assumed that the set of images are under /imgs folder in actual path")

args = parser.parse_args()
# Load the JSON annotations - for each one json file ...
for json_fn in args.jsonfiles:
  annotations = json.loads(open(json_fn).read())
  #for each one img file ...
  for data in annotations:
    fn = 'imgs/'+ data['filename'] 
    print 'Processing {}'.format(fn)
    if data['annotations']:
      # We're only interested in the classes of tags indicated ins args
      #for each one class of tag ... 
      for annotation in data['annotations']:
          tag = annotation ['class']
          if tag in args.tags:
              points = annotation             
              print points              
              for size in args.sizes:#for each one windows size ...
   
                  xleft =  points['x'] - (size /2) - 1
                  yupper =  points['y'] - (size /2) - 1
                  xright = points['x'] + (size /2) -1
                  ylower =  points['y'] + (size /2) -1                  
                 
                  # TODO check for out of range in the image
                  box = map(int, [xleft, yupper, xright, ylower])
                                    
                  im = Image.open(fn)
                  cropped=im.crop(box)
                  
                  #make new dir with the name of the tag and the size
#                  outdir=os.path.dirname(fn) +'/'+ tag + str(size) +'x'+ str(size)
                  outdir="{}/{}{}x{}".format(os.path.dirname(fn),tag,size,size)
                  if not os.path.exists(outdir):
                      os.makedirs(outdir)
                  
                  #make new file name to save the cropped image
                  orginalfn=os.path.basename(fn)              
#                  croppedfn=os.path.splitext(orginalfn)[0]+'_s'+ str(size) +'_point'+ str(int(points['x'])) +'-'+ str(int(points['y'])) +  os.path.splitext(orginalfn)[1]
                  croppedfn="{}_s{}_p{}-{}{}".format(os.path.splitext(orginalfn)[0],size,int(points['x']),int(points['y']),os.path.splitext(orginalfn)[1])
                  outdirfn=outdir+'/'+croppedfn
                  cropped.save(outdirfn)
                  print 'saved in '+ outdirfn
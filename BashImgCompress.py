from __future__ import print_function
import os, sys
from PIL import Image

def GetFileFromThisRootDir(dir,ext = None):
  allfiles = []
  needExtFilter = (ext != None)
  for root,dirs,files in os.walk(dir):
    for filespath in files:
      filepath = os.path.join(root, filespath)
      extension = os.path.splitext(filepath)[1][1:]
      if needExtFilter and extension in ext:
        allfiles.append(filepath)
      elif not needExtFilter:
        allfiles.append(filepath)
  return allfiles

Results = GetFileFromThisRootDir(os.getcwd(),ext=['jpg'])

size = (128, 128)

for infile in Results:
    outfile = os.path.splitext(infile)[0] + ".thumbnail" + os.path.splitext(infile)[1]
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)
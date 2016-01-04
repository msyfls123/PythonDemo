import os
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

Name = raw_input("Enter File Types:\n")
Paths = Name.split(",")
Results = GetFileFromThisRootDir(os.getcwd(),ext=Paths)
for i in Results:
  print i
raw_input('Fine?')
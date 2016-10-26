import kNN
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy import *
from PIL import Image

reload(kNN)
datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 25.0*array(datingLabels))
plt.savefig('./myFig.jpg')
# plt.show()

im = Image.open('./myFig.jpg')
im.show()

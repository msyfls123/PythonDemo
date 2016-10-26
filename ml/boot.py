import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

reload(kNN)
datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
# print datingDataMat,datingLabels[:20]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 25.0*array(datingLabels))
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), [[0.9, 0.1, 0.9]])
plt.show()

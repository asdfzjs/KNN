import numpy
import matplotlib
import matplotlib.pyplot as plt
import kNN
reload(kNN)
datingDataMat,datingLabels=kNN.file2matrix('datingTestSet2.txt')
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels))
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels))
plt.show()
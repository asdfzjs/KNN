#-*-coding:utf-8-*-
from numpy import *
import operator
from os import listdir
#收集数据，准备数据，分析数据，训练算法，测试算法，使用算法

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

#用于分类的输入向量：inX,输入的训练样本集合为：dataSet,标签向量为:labels,最后的参数k是用于选择最近邻居的数目
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]   #shape[0]就是读取矩阵第一维度的长度,计算矩阵有多少行
 #   print tile(inX, (dataSetSize,1))  #生成4行一列的矩阵
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    print diffMat
    sqDiffMat = diffMat**2
    print sqDiffMat
    sqDistances = sqDiffMat.sum(axis=1) #将一个矩阵的每一行向量相加
    print sqDistances
    distances = sqDistances**0.5    #开方
    print distances
    sortedDistIndicies = distances.argsort()   #argsort函数返回的是数组值从小到大的索引值
    print sortedDistIndicies
    classCount={}  #定义了一个字典
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)   #operator.itemgetter(1)取下标索引值是1的进行排序，true是降序
    return sortedClassCount[0][0]

#从文本中解析数据
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)  #取得文件行数
    returnMat = zeros((numberOfLines,3))   #生成numberOfLines行，3列的0矩阵
    classLabelVector  = []
    index = 0
    for line in arrayOLines:
        line = line.strip()  #移除字符串头尾的空格
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]   #属性存在矩阵里面
        classLabelVector.append(int(listFromLine[-1]))   #分类结果也存起来
        index += 1
    return returnMat,classLabelVector

#归一化特征值  newValue = (oldValue - min)/(max-min)
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))  #创建与样本集一样大小的零矩阵
    m = dataSet.shape[0]  #shape[0]就是读取矩阵第一维度的长度
    normDataSet = dataSet - tile(minVals,(m,1))  #样本集中的元素与最小值的差值
    normDataSet = normDataSet/tile(ranges,(m,1))  #数据相除，归一化
    return normDataSet,ranges,minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "the classifier came back with: %d,the real answer is :%d" % (classifierResult,datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    print errorCount
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))

if __name__=="__main__":
   # group,labels = createDataSet()
   #print classify0([0,0],group,labels,3)
   #datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
   #print datingDataMat[0:20]
   #autoNorm(datingDataMat)
   datingClassTest()


#-*-coding:utf-8-*-
from numpy import *
import operator

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


if __name__=="__main__":
    print("main")
    group,labels = createDataSet()
    print classify0([0,0],group,labels,3)
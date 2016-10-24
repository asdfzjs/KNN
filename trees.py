#-*-coding:utf-8-*-
'''
log(a)(M÷N)=log(a)(M)-log(a)(N);
信息熵的大小指的的是了解一件事情所需要付出的信息量是多少
信息熵衡量的是在你知道一个事件的结果后平均会给你带来多大的信息量
entropy(P1,P2,...,P32)=-(1/32)log(1/32)-(1/32)log(1/32)......-(1/32)log(1/32)
                                  =5/32+5/32...+5/32
                                  =(5*32)/32
                                  =5
'''
from math import log
import operator

#初始化一些数据
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

#计算信息熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  #数据量
    labelCounts = {}   #定义一个字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        else:
            labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/float(numEntries)
        shannonEnt -= prob*log(prob,2)
    return shannonEnt

def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet



if __name__=="__main__":
    dataSet,labels = createDataSet()
    #print dataSet
    #print calcShannonEnt(dataSet)
    retDataSet = splitDataSet(dataSet,0,0)
    print retDataSet
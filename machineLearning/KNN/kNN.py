#!/usr/bin/python
#-*- coding:utf-8 -*-

from numpy import *
import operator
from os import listdir

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B'];
    return group,labels

def classify0(inX,dataSet, labels, k):
	#得到数组的行数。即知道有几个训练数据
    dataSetSize = dataSet.shape[0]
	#tile将原来的一个数组，扩充成了4个一样的数组。diffMat得到了目标与训练数值之间的差值。
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    #print "diffMat",diffMat
    sqDiffMat=diffMat**2
	#对应列相加，即得到了每一个距离的平方
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
	#升序排序
    sortedDistIndicies=distances.argsort()
	#选择距离最小的k个点
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
	#排序
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
	
def file2matrix(filename):
	fr=open(filename)
	#get the number of lines in the file
	numberOfLines=len(fr.readlines())
	#print "numberOfLines:",numberOfLines
	#prepare matrix to return 
	returnMat=zeros((numberOfLines,3))
	#print "returnMat:",returnMat
	#prepare labels
	classLabelVector=[]
	fr=open(filename)
	index=0
	for line in fr.readlines():
		line=line.strip()
		listFromLine=line.split('\t')
		returnMat[index,:]=listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index+=1
	return returnMat,classLabelVector	
#归一化特征值
def autoNorm(dataSet):
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	ranges=maxVals-minVals
	normDataSet=zeros(shape(dataSet))
	m=dataSet.shape[0]
	normDataSet=dataSet-tile(minVals,(m,1))
	normDataSet=normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals
#测试
def datingClassTest():
	hoRatio=0.10
	datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals=autoNorm(datingDataMat)
	m=normMat.shape[0]
	numTestVecs=int(m*hoRatio)
	errorCount=0.0
	for i in range(numTestVecs):
		classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
		print "the classifier came back with:%d,the real answer is:%d" %(classifierResult,datingLabels[i])
		if(classifierResult != datingLabels[i]):
			errorCount += 1.0
	print "the total error rate is:%f" %(errorCount/float(numTestVecs)) 

#约会网站预测函数
def classifyPerson():
	resultList=['not at all','in small doses','ip large doses']
	percentTats=float(raw_input("percentage of time spent playing video games?"))
	ffMiles=float(raw_input("frequent flier miles earned per year?"))
	iceCream=float(raw_input("liters of ice cream consumed per year?"))
	datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals=autoNorm(datingDataMat)
	inArr=array([ffMiles,percentTats,iceCream])
	classifierResult=classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
	print "you will probably like this person:",resultList[classifierResult-1]

#将图像转为向量
def img2vector(filename):
	returnVect=zeros((1,1024))
	fr=open(filename)
	for i in range(32):
		lineStr=fr.readline()
		for j in range(32):
			returnVect[0,32*i+j]=int(lineStr[j])
	return returnVect
#手写数字识别系统的测试代码
def handwritingClassTest():
	hwLabels=[]
	trainingFileList=listdir('trainingDigits')
	m=len(trainingFileList)
	trainingMat=zeros((m,1024))
	for i in range(m):
		fileNameStr=trainingFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumStr=int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:]=img2vector('trainingDigits/%s' % fileNameStr)
	testFileList=listdir('testDigits')
	errorCount=0.0
	mTest=len(testFileList)
	for i in range(mTest):
		fileNameStr=testFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumStr=int(fileStr.split('_')[0])
		vectorUnderTest=img2vector('testDigits/%s' % fileNameStr)
		classifierResult=classify0(vectorUnderTest,trainingMat,hwLabels,3)
		print "the classifier came back with:%d,the real anser is %d " % (classifierResult,classNumStr)
		if(classifierResult!=classNumStr): errorCount+=1.0
	print "\nthe total numberof errors is:%d" % errorCount
	print "\nthe total error rate is %f" % (errorCount/float(mTest))

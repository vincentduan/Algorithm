#!/usr/bin/python
#-*- coding:utf-8 -*-

from numpy import *
import operator

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B'];
    return group,labels

def classify0(inX,dataSet, labels, k):
	#得到数组的行数。即知道有几个训练数据
    dataSetSize = dataSet.shape[0]
	#tile将原来的一个数组，扩充成了4个一样的数组。diffMat得到了目标与训练数值之间的差值。
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    print "diffMat",diffMat
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
	print "numberOfLines:",numberOfLines
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

#!/usr/bin/python
#-*- coding:utf-8 -*-

from math import log
import operator

#计算给定数据集的熵
def calcShannonEnt(dataSet):
	numEntries=len(dataSet)
	labelCounts={}
	for featVec in dataSet:
		currentLabel=featVec[-1]
		#print currentLabel
		#print featVec
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel]=0
		labelCounts[currentLabel]+=1
	shannonEnt=0.0
	#print labelCounts
	for key in labelCounts:
		prob=float(labelCounts[key])/numEntries
		#print prob,key
		shannonEnt -= prob*log(prob,2)
	return shannonEnt
	
def createDataSet():
	dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels=['no serfacing','flippers']
	return dataSet,labels
#按照给定特征划分数据集
def splitDataSet(dataSet,axis,value):
	retDataSet=[]
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec=featVec[:axis]
			#print "reducedFeatVec",reducedFeatVec
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet
#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
	numFeatures=len(dataSet[0]) - 1
	baseEntropy=calcShannonEnt(dataSet)
	bestInfoGain=0.0
	bestFeature=-1
	for i in range(numFeatures):
		#创建唯一的分类标签列表
		featList=[example[i] for example in dataSet]
		#print featList,i
		uniqueVals=set(featList)
		newEntropy=0.0
		for value in uniqueVals:
			subDataSet=splitDataSet(dataSet,i,value)
			prob=len(subDataSet)/float(len(dataSet))
			newEntropy+=prob*calcShannonEnt(subDataSet)
		infoGain=baseEntropy-newEntropy
		if(infoGain>bestInfoGain):
			bestInfoGain=infoGain
			bestFeature=i
	return bestFeature

def majorityCnt(classList):
	classCount={}
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote]=0
		classCount[vote]+=1
	sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

#创建树的函数代码
def createTree(dataSet, labels):
	classList=[example[-1] for example in dataSet]
	if classList.count(classList[0])==len(classList):
		return classList[0]
	if len(dataSet[0])==1:
		temp=majorityCnt(classList)
		print temp
		return temp
	bestFeat=chooseBestFeatureToSplit(dataSet)
	bestFeatLabel=labels[bestFeat]
	myTree={bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues=[example[bestFeat] for example in dataSet]
	uniqueVals=set(featValues)
	for value in uniqueVals:
		subLabels=labels[:]
		myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
	return myTree

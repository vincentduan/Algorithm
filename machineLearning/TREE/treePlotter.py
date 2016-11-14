#!/usr/bin/python
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt

#定义文本框和箭头格式
decisionNode=dict(boxstyle="sawtooth",fc="0.8")
leafNode=dict(boxstyle="round4",fc="0.8")
arrow_args=dict(arrowstyle="<-")

#绘制带箭头的注释
def plotNode(nodeTxt,centerPt, parentPt, nodeType):
	createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction', va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

def createPlot():
	fig=plt.figure(1, facecolor='white')
	fig.clf()
	createPlot.ax1=plt.subplot(111, frameon=False)
	print "决策"
	plotNode(U'决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
	plotNode(U'叶节点', (0.8, 0.1), (0.3, 0.8), leafNode)
	plt.show()

#获取叶节点的数目和树的层数
def getNumLeafs(myTree):
	numLeafs=0
	firstStr=myTree.keys()[0]
	secondDict=myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			numLeafs += getNumLeafs(secondDict[key])
		else:
			numLeafs+=1
	return numLeafs
def getTreeDepth(myTree):
	maxDepth=0
	firstStr=myTree.keys()[0]
	secondDict=myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			thisDepth=1+getTreeDepth(secondDict[key])
		else:
			thisDepth=1
		if thisDepth > maxDepth:
			maxDepth=thisDepth
	return maxDepth

def retrieveTree(i):
	listOfTrees=[{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}},{'no surfacing':{0:'no',1:{'flippers':{0:{'head':{0:'no',1:'yes'}},1:'no'}}}}]
	return listOfTrees[i]

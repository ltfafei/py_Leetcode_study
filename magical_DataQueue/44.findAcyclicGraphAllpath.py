#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
44、找到无环图中所有的路径
    输入一个二维列表g，列表中的g[i]子列表表示图中第i个结点可以触达到的子节点，定义默认的起始结点为0，
若输入列表g为[[1,2], [3], [4], [4]]，构成如44-1图所示，此图的所有路径为[[0,1,3,4], [0,2,4]]。
解题思路：
    由于某个结点对应的子节点就是输入列表中对应位置的元素所描述的，所以解决此题非常适合回溯法。每当一条
路径的当前结点确定后，我们即可从列表中找到对应的子节点组，进行递归和回溯即可。
'''

def findAcycliGraphTar(graph):
    res = []  #结果列表
    #定义递归函数，构建路径
    def getPath(path, nextNodesIndex):
        #如果不再有子节点，则当前路径构建结束
        if nextNodesIndex >= len(graph) or len(graph[nextNodesIndex]) == 0:
            res.append(list(path))
            return
        #将当前结点的子节点取出
        nodes = graph[nextNodesIndex]
        #遍历子结点列表，分别构建路径
        for n in nodes:
            #采用回溯法
            tmp = list(path)
            tmp.append(n)
            getPath(tmp, n)
        getPath([0], 0)
        return res
#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
41.1、计算二叉树路径的和
    树路径的和是指从树的根节点开始一直到某个叶子结点为止所经过的所有结点值的和。现在输入一个二叉树的
根节点和一个目标数值，需要检查输入的二叉树中是否有某个路径的和等于输入的目标数值，如果存在这样的路径
，则返回True，否则返回False。
解题思路：
（1）定义一个递归函数，其参数为树节点，返回值为其中所有路径和组成的列表；
（2）如果递归函数输入的树节点为空结点，则返回空列表；
（3）如果递归函数输入的树节点为叶子结点，则将当前结点的值放入列表返回；
（4）如果递归函数输入的树节点不是叶子结点，则递归对左子树和右子树进行运算。
（5）将左子树和右子树得到的结果进行遍历，加上当前结点的值构成新结果列表返回。最后判断最终结果列表中
是否包含输入的目标树。
'''

def binSum(root, sum):
    #定义递归函数
    def treeValue(tree):
        #如果是空树，直接返回空列表
        if tree == None:
            return []
        #递归对左右子树进行运算
        leftList = treeValue(tree.left)
        rightList = treeValue(tree.right)
        res = []
        #结果列表构建
        if len(leftList) == 0 and len(rightList) == 0:  #如果左右子树，直接添加到列表
            res.append(tree.value)
        else:
            #对左子树路径遍历
            for n in leftList:
                res.append(tree.value + n)
            #对右子树路径遍历
            for n in rightList:
                res.append(tree.value + n)
        return res
    resList = treeValue(root)
    #判断目标值是否在结果列表中
    if sum in resList:
        return True
    return False

'''
41.2、计算树及所有子树的平均值
    定义：一棵树的平均值是这棵树中所有结点值的和除以结点个数得到的数值。现在，输入一棵树的根节点，
要求使用编程将这棵树的平均值及所有子树的平均值进行计算，并将结果组成列表返回。
解题思路：
    本题需要采用两个递归函数，第一个递归函数用来将所有结点值进行相加，并且根据结点个数计算出
平均值；第二个函数遍历计算所有子树的平均值。
'''

def maxAverageSubtree(root):
    #计算树的和
    def treeSum(tree):
        if tree == None:
            return 0
        i = 1  #结点个数
        #定义左右子树和
        sumL = 0
        sumR = 0
        #分别计算左右子树和
        if tree.left != None:
            o = treeSum(tree.left)
            sumL = o[0]
            i += o[1]
        if tree.right != None:
            o = treeSum(tree.right)
            sumR = o[0]
            i += o[1]
        return [sumL + sumR + tree.value, i]
    #计算树的平均值
    def allSubtreeAverage(tree):
        res = []
        if tree == None:
            return res
        res.append(treeSum(tree)[0]/treeSum(tree)[1])
        res += allSubtreeAverage(tree.left)
        res += allSubtreeAverage(tree.right)
        return res
    return max(allSubtreeAverage(root))
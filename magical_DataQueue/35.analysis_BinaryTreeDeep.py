#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
35、解析二叉树深度（递归）
二叉树的几种结构：
（1）没有任何节点的二叉树为空二叉树；
（2）只有一个根节点的二叉树；
（3）只有左子树；
（4）只有右子树；
（5）左右子树都有。
    现在输入一个二叉树，要求编程解析其最大深度。二叉树的最大深度是指根节点到最远子节点的最长路径的
节点数。如果将二叉树画出来，二叉树的深度可以形象的理解为二叉树的层数。例如输入的二叉树节点定义如下：
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
'''

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def anBinaryTree(root):
    #定义递归函数，计算树的深度
    def deep(tree):
        #如果当前节点为空树，则返回深度0
        if tree == None:
            return 0
        #选取当前节点左右子树中深度较深的加1作为当前节点的深度
        return max(deep(tree.left), deep(tree.right)) + 1
    return deep(root)

'''
解析二叉树的最小深度
    二叉树的最小深度是指从根节点到最近的叶子节点所经过的节点树。现在要求编程求二叉树的最小深度
注意：最小深度的定义是从根节点到叶子节点，叶子节点的定义是没有任何子节点的节点的。
'''

def minBinaryTree(root):
    def deep(tree):
        #如果当前节点为空树，则返回深度0
        if tree == None:
            return 0
        #左右子树都没有，则最小深度为1
        if tree.left == None and tree.right == None:
            return 1
        #只有右子树在，则计算右子树的最小深度
        if tree.left == None:
            return deep(tree.right) + 1
        #只有左子树在，则计算左子树的最小深度
        if tree.right == None:
            return deep(tree.left) + 1
        #如果左右子树都在，则分别计算深度并选择较小的子树深度
        return min(deep(tree.left), deep(tree.right)) + 1
    return deep(root)

'''
解析N叉树的深度
    假设题目中输入的树结构是N叉树，即一个父节点下面可能有多个子树，则如何解析出N叉树的最大深度
要求编程实现
'''

#定义N叉树结构
class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children  #children属性为列表，存放当前节点的所有子节点

def N_maxTreeDepth(root):
    #定义递归函数计算深度
    def deep(tree):
        if tree == None:
            return 0
        #如果没有children，返回深度1
        if tree.children == None:
            return 1
        l = []  #定义列表存储所有子树的深度
        #遍历所有子树，对其深度进行计算
        for t in tree.children:
            l.append(deep(t) + 1)
        if len(l) == 0:
            return 1
        return max(l)  #将最大深度返回
    return deep(root)
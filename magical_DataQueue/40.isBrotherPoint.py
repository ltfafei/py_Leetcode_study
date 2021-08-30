#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
40.判断是否为堂兄弟结点
堂兄弟结点定义：两个结点在同一层，但是其父节点不同。
    现在输入一颗二叉树的根节点，可以保证树中的所有元素的值都是唯一的。同时，输入两个结点的值，要求用
编程判断这两个值对应的结点是否为堂兄弟结点。
解题思路：
    首先需要根据输入值找到对应结点的位置，判断是否在同一层以及其父节点是否不同。
'''

def isBrother(root, x, y):
    #定义x值和y值对应结点的信息
    xNode = None
    yNode = None
    #定义递归函数
    #其中tree为当前结点，h为当前深度，n为要查找的值，father为父节点
    def findNode(tree, h, n, father):
        if tree == None:
            #返回的列表中第一个元素为找到的结点
            return [None, h, father]
        if tree.value == n:
            return [tree, h, father]
        if findNode(tree.left, h+1, n, tree)[0] != None:
            return findNode(tree.left, h+1, n, tree)
        else:
            return findNode(tree.right, h+1, n, tree)

    xNode = findNode(root, 0, x, None)
    yNode = findNode(root, 0, y, None)
    #判断是否是堂兄弟结点。xNode[1]第二个元素表示层，xNode[2]第三个元素表示父节点
    if xNode != None and yNode != None and xNode[1] == yNode[1] and xNode[2] != yNode[2]:
        return True
    return False
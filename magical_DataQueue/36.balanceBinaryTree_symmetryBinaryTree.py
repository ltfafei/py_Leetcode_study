#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
36.1、平衡二叉树的判定
    输入一个二叉树的根节点，要求尝试编程判断此二叉树是否是平衡二叉树。对于一个二叉树来书，如果其中
任意节点的左右子树的最大深度相差不超过1，则这棵二叉树就是平衡二叉树。
解题思路：树本身是一种递归结构，解决与树相关的问题时，也是采用递归函数。
（1）定义一个递归函数，专门用来计算一棵树的最大深度；
（2）定义一个解析二叉树是否平衡的递归函数，判定二叉树是否平衡。
'''

#计算树最大深度的函数
def deep(tree):
    if tree == None:
        return 0
    return max(deep(tree.left), deep(tree.right)) + 1
#入口函数
def blanceBinary(tree):
    #定义内部递归函数，用来解析当前节点是否平衡
    if tree == None:
        return True
    #左右子树绝对值只差大于1，不满足条件
    if abs(deep(tree.left) - deep(tree.right)) > 1:
        return False
    return blanceBinary(tree.left) and blanceBinary(tree.right)

'''
36.2、对称二叉树的判定
    对称二叉树是一种非常特殊的二叉树，对称的二叉树是镜像的，即：将二叉树中每个结点的左右子树交换
位置后，得到的新的二叉树与原始的二叉树完全一样。
'''

def isSymmetry(root):
    #定义递归函数进行对称性判定
    def isSyme(tree):
        #空树认为是对称的
        if tree == None:
            return True
        #只有父节点的树也是对称的
        if tree.left == None and tree.right == None:
            return True
        #树结构是否对称判定
        if tree.left == None or tree.right == None:
            return False
        #子树值是否对称判定
        if tree.left.value != tree.right.value:
            return False
        #子树结构是否对称判定
        if tree.left.left == None and tree.right.right != None:
            return False
        if tree.left.left != None and tree.right.right == None:
            return False
        if tree.left.right == None and tree.right.left != None:
            return False
        if tree.left.right != None and tree.right.left == None:
            return False
        #子树值是否对称判定
        if tree.left.left != None and tree.right.right != None:
            if tree.left.left.value != tree.right.right.value:
                return False
        if tree.left.right != None and tree.right.left != None:
            if tree.left.right.value != tree.right.right.value:
                return False
        #构造新的树，递归进行对称性判定
        tmp = tree.left.right
        tree.left.right = tree.right.right
        tree.right.right = tmp
        return isSyme(tree.left) and isSyme(tree.right)
    return isSyme(root)
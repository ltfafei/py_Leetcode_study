#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
38.1、通过遍历构造二叉树
    现在，假设有一组前序遍历和后续遍历的二叉树结果列表，要求编程通过这些数据构造出满足条件的二叉树
例如：如果输入的两个列表为：[3, 1, 3, 1, 7, 3, 1]和[3, 1, 1, 3, 1, 7, 3]，则可以构造如图38-1所示的
二叉树。
解题思路：
    当一颗二叉树中所有结点的值都唯一时，由其前序遍历和后序遍历的结果是很容易推导出对应的二叉树的。关于
前序遍历和后序遍历的过程，前面也实现过。前序遍历结果列表中的第1个值一定是二叉树的根节点值，第2个值一定
是二叉树当前结点左子树根节点的值，假设其为n，对于后序遍历来说，是从左子树先开始遍历，因此可以在后序遍历
结果中找到值n，以此n值所在的位置为分界线，可以将前序遍历和后序遍历的结果列表分别拆分成左子树的遍历结果
和右子树的遍历结果，后面只要递归进行左右子树的处理即可。
'''

#定义树节点结构
class builtBinTree:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
#定义递归函数。pre: 前序遍历列表，last: 后序遍历列表
def builtBinaryTree_1(pre, last):
    #递归结束判定，列表为空代表递归结束
    if len(pre) == 0:
        return None
    root = builtBinTree(pre[0])  #创建根节点
    #如果没有其他子结点则返回根节点
    if len(pre) == 1:
        return root
    count = len(pre)  #当前总结点个数
    leftCount = 0  #当前左子树节点个数
    leftValue = pre[1]  #当前左子树根结点的值
    #后序遍历寻找左子树结点的位置
    for n in range(len(last)):
        if last[n] == leftValue:
            leftCount = n
    #1:leftCount+2截取左子树前序遍历结果，0:leftCount+1截取左子树后序遍历结果
    root.left = builtBinaryTree_1(pre[1:leftCount+2], last[0:leftCount+1])
    #leftCount+2:count截取右子树前序遍历结果，leftCount+1:count-1截取右子树后序遍历结果
    root.right = builtBinaryTree_1(pre[leftCount+2:count], last[leftCount+1:count-1])
    return root

'''
38.2、通过有序列表构造二叉搜索树
    一颗二叉搜索树有这样的性质：
（1）它可以是一颗空树；
（2）如果它不是一颗空树，则其左子树上所有结点的值都小于其根节点的值，其右子树上所有结点的值都
大于其根节点的值。如图38-2
    现在输入一个有序列表，要求编程构造一颗二叉搜索树，且要求每个结点的左右子树高度差不超过1。
解题思路：
（1）对二叉树进行中序遍历，可以发现其遍历的结果就是一个有序列表。所以如果要从一个有序列表构造
出二叉搜索树，只需要任选列表中一个值作为根节点，在列表中，此值左侧的元素用来构建根节点的左子树
此值右侧的元素用来构建根节点的右子树即可；
（2）要满足任意结点的左右子树高度差不超过1这个条件，那么只需要保证选取中间元素作为根节点即可。
如果元素个数是偶数，则中间元素可向下取整。
'''

def builtBinaryTree_2(l):
    #递归结束判定
    if len(l) == 0:
        return None
    mid = int(len(l) / 2)  #获取列表中间元素位置
    root = builtBinTree(l[mid])   #创建根节点
    #递归创建左右子树
    root.left = builtBinaryTree_2(l[:mid])
    root.right = builtBinaryTree_2(l[mid+1:])
    return root
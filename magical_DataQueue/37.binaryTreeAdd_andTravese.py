#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
37.1、二叉树相加
    现在定义，两个二叉树相加规则如下：
（1）对于同一个位置上的节点，如果一棵树为空，一棵树不为空，则相加的结果取不为空的当前节点；
（2）如果同一个位置上的结点两棵树都不为空，则将其存储的值相加后作为结果存取此位置节点。
解题思路：
（1）定义一个递归函数，处理结点的相加操作；定义根节点变量，取输入的两个结点中任意一个不为空
的结点作为根节点；
（2）进行根节点的值的计算逻辑，将输入的两个结点的值相加；
（3）调用递归函数，将输入的两结点的左子结点相加重新赋值到根节点；
（4）调用递归函数，将输入的两结点的右子结点相加重新赋值到根节点；
'''

def binaryTreeAdd(n1, n2):
    root = None  #定义新树的根节点
    #定义左右子树的值
    v1 = 0
    v2 = 0
    #只有左子树，获取左结点的值
    if n1 != None:
        root = n1
        v1 = n1.value
    #只有右子树获取右结点的值
    if n2 != None:
        root = n2
        v2 = n2.value
    #获取左右子树之和
    if root != None:
        root.value = v1 + v2
    else:
        return None
    #定义两个子节点，一个子节点分为左子树和右子树
    l1 = None
    r1 = None
    l2 = None
    r2 = None
    if n1 != None:
        l1 = n1.left
        r1 = n1.right
    if n2 != None:
        l2 = n2.left
        r2 = n2.right
    #子树相加
    root.left = binaryTreeAdd(l1, l2)
    root.right = binaryTreeAdd(r1, r2)

#二叉树的遍历
'''
37.2、二叉树的前序遍历
前序遍历：先遍历根结点，再遍历左节点，最后遍历右节点。
    输入一个二叉树的根节点，要求使用前序遍历的方式将二叉树存储后的数据转换为列表输出。如图37-1所示
的二叉树，遍历后的结果为[3,1,7,3,1]
'''

def preorderTraverse(root):
    #递归函数，将遍历的结点转换成列表
    def transList(tree):
        #空树直接返回空列表
        if tree == None:
            return []
        l = []
        #按照遍历顺序依次添加到列表中
        l.append(tree.value)
        #对左右子树进行遍历
        l += transList(tree.left)
        l += transList(tree.right)
        return l
    return transList(root)  #调用递归函数

'''
37.3、分层遍历二叉树
    在实际情况中，并非所有对二叉树的遍历需求都是符合二叉树结构的。假设可以按照层的顺序，从上到下，从
左到右对二叉树进行遍历。现在要求使用这种方式将二叉树存储的数据遍历出来存入列表。例如37-3所示的二叉树
遍历结果为：[3, 1, 7, 3, 1, 3, 1]。
解题思路：
    定义递归函数对一层结点进行遍历取值，并将每个结点的子节点进行存储，递归进行下一层遍历。
'''

def levelOrderBinaryTree(root):
    #定义递归函数遍历结点组
    def enumNodeList(nodeList):
        #结点组为空，则递归结束
        if len(nodeList) == 0:
            return None
        nextNodeList = []  #存储下次需要遍历的结点
        res = []  #结果列表
        l = []   #当前层遍历出的结果
        #遍历当前层中结点的值
        for node in nodeList:
            l.append(node.value)
            if node.left != None:
                nextNodeList.append(node.left)
            if node.right != None:
                nextNodeList.append(node.right)
        #将遍历结果追加到结果列表
        res += 1
        #递归遍历
        next = enumNodeList(nextNodeList)
        if next != None:
            res += next
        return res
    #判断是否是空树
    if root == None:
        return []
    return enumNodeList([root])
#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
42、完全二叉树的结点个数
完全二叉树定义：除了最底层的结点可以不填满外，其余每层结点数都需要达到最大值，并且，最底层的结点是按顺序
从左往右进行填充的。
    现在输入一个完全二叉树的根节点，要求编程求出当前二叉树的结点个数。
'''

#常规遍历法
def entryBintreePoint_1(root):
    def count(tree):
        if tree == None:
            return 0
        return 1 + count(tree.left) + count(tree.right)
    return count(root)

'''
程序优化：
    通过分析二叉树的性质可以发现，除了最后一层外，其每一层的结点个数与层数是有关系的。如果
当前为h层，则此层的结点个数为：2^(h-1)，因此，对于完整的完全二叉树，可以使用该公式直接计算
得到其结点个数。
    对于输入的完全二叉树来说，如果左子树的层数和右子树的层数相同，则其左子树一定是满的，可以
用公式直接计算左子树的结点个数，再递归计算右子树的结点个数再进行相加即可。如果左子树和右子树
的层数不同,则右子树一定是满的，可以使用公式计算右子树的结点个数，在加上左子树的结点个数即可。
'''

def entryBintreePoint_2(root):
    #计算完全二叉树的层数
    def deep(tree):
        f = 0
        if tree == None:
            return f
        f += 1 + deep(tree.left)
        return f
    #计算二叉树结点个数
    def count(tree):
        if tree == None:
            return 0
        return 1 + count(tree.left) + count(tree.right)
    if root == None:
        return 0
    #分别计算左右子树高度
    deepL = deep(root.left)
    deepR = deep(root.right)
    #高度相同，左子树是满的
    if deepL == deepR:
        c = 1
        while deepL > 0:
            c += 2 ** (deep-1)
            deepL -= 1
            return c + count(root.right)
    #高度不同，则右子树是满的
    else:
        c = 1
        while deepR > 0:
            c += 2 ** (deepR -1)
            deepR -= 1
        return c + count(root.left)
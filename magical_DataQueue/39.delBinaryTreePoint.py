#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
39.1、删除二叉搜索树结点
    输入一个二叉搜索树的根节点和一个值，要求编程将二叉搜索树中此值的结点删除，并且将新的二叉树的根节点
返回。注意：删除节点后的二叉树依然要保证是一颗二叉搜索树。
解题思路：
    对于一颗二叉搜索树来书，要删除其中一个结点并使其性质保持不变，要分4中情况讨论。
情况1：需要删除的结点没有左子树也没有右子树；没有左子树也没有右子树的结点为叶子结点，要删除叶子结点，直接
将其置空即可。
情况2：如果要删除的结点只有左子树，则直接将当前结点删除，使用当前结点的左子树代替当前结点的位置即可；
情况3：第3种情况和第二种情况对应，要删除的结点只有右子树，则直接将当前结点删除，使用当前结点的右子树
代替当前结点的位置即可；
情况4：需要删除的结点既有左子树，也有右子树。这种情况是最难处理的一种，根据二叉树的性质，当删除当前
结点后，需要选择其左子树的根节点或右子树的根节点填充到当前位置，如果选择了使用左子树填充，则需要将
右子树补充到左子树最靠右的一个叶子结点上。同理，如果选择使用右子树填充，则需要将左子树补充到最靠左
的一个叶子结点上。
'''

#情况4实现
def delBinaryTree_1(root, key):
    #定义递归函数删除树中结点
    def delte(tree, value):
        #空树直接返回None
        if tree == None:
            return None
        #如果当前结点不是要删除的结点，递归对左右子树进行处理
        if value != tree.value:
            tree.left = delte(tree.left, value)
            tree.right = delte(tree.right, value)
            return tree
        root = None
        #如果当前结点是要删除的结点，选择左子树进行填充
        if tree.left != None:
            root = tree.left
            tmp = tree.left
            while tmp.right != None:
                tmp = tmp.right
            tmp.right = tree.right
        # 如果当前结点是要删除的结点，选择右子树进行填充
        elif tree.right != None:
            root = tree.right
            tmp = tree.right
            while tmp.left != None:
                tmp = tmp.left
            tmp.left = tree.left
        return root
    return delte(root, key)

'''
39.2、删除二叉树中指定叶子结点
    输入一颗二叉树的根节点和一个数值n，现在要求通过编程将此二叉树中所有数值为n的叶子结点都删除
掉，注意：需要使用递归函数，并且最终返回的结果中将不存在数值为n的叶子结点。
解题思路：
    使用递归+循环的思路，递归用来找到需要删除的叶子结点的值，进行删除操作；循环用来将删除某个
叶子结点后新产生的符合条件的叶子结点在进行删除。编写递归函数时，需要遵循这样的思路：首先需要
能够找到当前树中所有满足条件的叶子结点进行删除操作，其次要将是否进行了删除操作进行标记，如果
有删除操作，则表明可能产生新的符合条件的结点，需要再次循环调用递归函数进行处理。
'''

def delBinaryTree_2(root, target):
    #定义递归函数删除指定结点
    def delTarget(tree, value):
        #如果为空树，直接返回None
        if tree == None:
            return [None, False]  #第一个元素表示处理后的树，第二个元素标记是否进行了删除操作
        # 定义标记左右叶子结点
        leftem = [None, False]
        rightem = [None, False]
        #如果不是叶子结点，则进行递归处理
        if tree.left != None or tree.right != None:
            if tree.left != None:
                leftem = delTarget(tree.left, value)
            if tree.right != None:
                rightem = delTarget(tree.right, value)
            tree.left = leftem[0]
            tree.right = rightem[0]
            return [tree, leftem[1] or rightem[1]]
        #如果当前结点是叶子结点，判断是否需要进行删除操作
        if value == tree.value:
            return [None, True]
        else:
            return [tree, False]
        item = [root, True]
        #循环进行叶子结点的删除操作
        while item[1]:
            item = delTarget(item[0], target)
        return item[0]
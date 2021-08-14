#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
7、列表中最长的连续递增序列
    现在输入一个列表，列表中存放的全部为整数元素，要求编写程序，将其中最长递增序列子列表返回。例如：输入列表为
[4,3,5,7,2,5]，则需要返回[3,5,7]作为结果。
解题思路：
    可以通过对输入的列表进行一次遍历解决。首先需要使用一个临时变量记录当前已经积累的最长递增序列的长度。另一个
变量记录当前遍历到的元素所在的递增序列的长度，一轮遍历完成后，可以将最长的递增子序列找到，将其返回即可。
'''

def longestContinseque(l):
    #列表为空的情况
    if len(l) == 0:
        return 0
    pre = l[0]   #记录上一个元素
    curCount = 1  #遍历到元素的个数
    curList = [l[0]]  #遍历的列表
    maxC = 1     #记录当前遍历到的递增子列表长度
    maxL = [pre]   #临时列表，记录当前遍历到的递增元素
    for i in range(1, len(l)):
        item = l[i]
        #符合递增场景
        if item > pre:
            curCount += 1
            curList.append(item)
        #重置计算
        else:
            curCount = 1
            curList = [item]
        pre = item
        if maxC < curCount:
            maxC = curCount
            maxL = curList
    return maxL

print(longestContinseque([4,3,5,7,2,5]))
'''
Output result：
    [3, 5, 7]
'''
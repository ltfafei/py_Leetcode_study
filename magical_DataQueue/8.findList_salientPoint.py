#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
8、寻找列表的凸点
    现在定义，当整数列表中某个元素既大于其左侧的值又大于其右侧的值时，就称这个元素所在的位置为列表的凸点。一个列表
可能存在多个凸点，只需要找到任意一个的位置返回即可。注意：输入的列表规模可能会非常大（其中元素个数非常多），并且
可以确定，列表中不存在两个连续且相等的元素。现在要求通过编程找到列表中的一个凸点。例如输入列表：[1,2,3,2,0]，则
需要返回索引位置2，即元素3所在的位置。由于列表元素可能个数庞大，需要尽量提升算法的效率。
解题方法：
（1）循环遍历（时间复杂度：O(n)）
（2）二分法
'''

def findL_saliPoint_1(l):
    #列表小于三个元素情况
    if len(l) < 3:
        return ""
    pre = l[0]  #记录当前的上一个元素
    for i in range(len(l)):
        item = l[i]
        #凸点判断
        if item < pre:
            return i - 1
        pre = item

print(findL_saliPoint_1([1,2,4,3,4,2,0]))
'''
Output result：
    2
'''

def findL_saliPoint_2(li):
    #列表小于三个元素情况
    if len(li) < 3:
        return ""
    l = 0   #左边界
    r = len(li) - 1    #又边界
    while l < r:
        m = int((l + r) / 2)   #二分
        #凸点再右边情况
        if li[m] > li[l]:
            l = m
        # 凸点再左边情况
        else:
            r = m
    return l

print(findL_saliPoint_2([1,2,3,2,0]))
'''
Output result：
    2
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
12.1、列表分割
    输入一个列表，要求找到一个位置将列表分成左右两个子列表。分割的子列表需要满足如下条件：
左列表的所有元素都不大于右列表中的任意元素；左右列表都非空；如果有多个可能的分割位置，选择较小的一个作为答案。
要求编程实现：找到满足上述条件的位置。
解题方法：
方法一-暴力枚举：题中要求找到一个位置将列表分割开后满足左边列表的最大值不大于右边列表的最小值。理论上，只需要
遍历所有可能的分割点，对列表分割后条件检查，如果满足条件，直接将位置返回即可；
方法二：可以使用python的内置函数取列表的最大值和最小值，虽然依然有不小的性能消耗，可以在最值发生变化时在进行计算。
'''

'''
下面使用max()和min()方法，也是O(n)时间复杂度
方法一：
'''
def listCut_1(l):
    for i in range(1, len(l)):
        left = l[:i]
        right = l[i:]
        if max(left) <= min(right):
            return i-1
        else:
            return "Not exit"

print(listCut_1([2,3,5,2,3,7,4,9]))
'''
Output result：
    0
'''

#方法二：
def listCut_2(l):
    lMax = None  #定义最大值
    rMin = None  #定义最小值
    for i in range(1, len(l)):
        left = l[:i]
        right = l[i:]
        if lMax == None:
            lMax = max(left)
        #不等于None，追加到左边
        elif lMax < l[i-1]:
            lMax = l[i-1]
        if rMin == None:
            rMin = min(right)
        elif rMin >= l[i-1]:
            rMin = min(right)
        #比较
        if lMax <= rMin:
            return i-1

print(listCut_2([2,3,5,2,3,7,4,9]))
'''
Output result：
    0
'''

'''
12.2、冒泡排序（原地排序）
    冒泡排序最终排列成一个递增的列表，它的核心是对相邻的元素进行比较，如果顺序错误，就将两元素位置进行交换
所以对于冒泡排序，是从头到尾的一次遍历可以将最大值元素移动到列表末尾。
    现在，使用冒泡排序将输入的一个列表进行升序排列。例如：输入列表L为：[1,4,2,3,6,9]，将输出结果：
[1,2,3,4,6,9]
'''

def bubbleSort(L):
    #只需要遍历到len(L)-1位，因为len(L)-1位元素固定了，最后一位也就是有序的了
    for i in range(0, len(L)-1):
        #每次排序需要排序到哪一位
        for j in range(0, len(L)-1-i):
            i1 = L[j]
            i2 = L[j+1]
            #如果顺序错误，位置进行交换
            if i2 < i1:
                L[j+1] = i1
                L[j] = i2
    return L

print(bubbleSort([1,4,2,3,6,9]))
'''
Output result：
    [1, 2, 3, 4, 6, 9]
'''
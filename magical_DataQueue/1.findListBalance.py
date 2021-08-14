#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
1、寻找列表平衡点
    现在输入一组整数组成的列表。能否找到其中的一个位置，使得小于此位置下标的所有元素之和与大于此位置下标的所有
元素之和相等。如果可以找到，则返回这个位置，如果不能则返回False。例如：输入列表[1,2,6,10,4,5]，则返回3，因为
1+2+6=9，4+5=9，平衡点位于10这个位置，该位置索引为3。
解题思路：
（1）左右两边进行遍历累加进行判断；
（2）先将所有元素进行累加，然后通过左加右减的方式进行判断。
'''

def findListBalan(l):
    left = 0
    right = 0
    #列表中只有一个元素
    if len(l) <= 1:
        return False
    #将所有元素进行累加
    for i in l:
        right += i
    #遍历进行左加右减
    for i in range(len(l)):
        if i == 0:
            right -= l[i]
        else:
            right -= l[i]
            left += l[i-1]
        #如果左边和等于右边和，说明找到平衡点，返回索引
        if left == right:
            return i
    return False

print(findListBalan([1,2,6,10,4,5]))
'''
Output result：
    3
'''
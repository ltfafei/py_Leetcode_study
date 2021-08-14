#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
5、列表连续子序列之和最大值
    输入一个列表，列表中存放一组整数。要求找到列表中连续元素之和的最大值。例如：输入的列表为[-1,-2,-3,4,5,6,-1]，
则需要返回15作为结果，因为连续元素4，5，6的和最大。
解题方法：
（1）暴力暴力(两层循环，时间复杂度高，效率差)；
（2）程序优化：同号合并，再做循环。一定程度上减少了元素的个数，效率自然提高了(但是，合并时如果碰到一正一负的情况，
反而会让算法变得更加复杂)；
（3）动态规划：可以使用推到法来解决。假设使用index来表示元素的下标，使用F(index)表示以下标为index的元素结尾的连续
元素的最大值，则下标为index+1的元素(设元素为N)结尾的连续元素的最大值为F(index)+N，那么就是N。因此，通过动态规划的
公式，只需要将列表中每个位置的元素都假设成结尾元素计算其连续元素的最大值并保存，最终将所有计算结果的最大值返回即可。
'''

#暴力遍历
def maxSubsequeSum_1(l):
    if len(l) == 0:
        return 0
    ma = l[0]   #假设第一个元素就是最大值
    #遍历寻找最大序列
    for i in range(1, len(l)):
        tmp = l[i]  #外层临时值
        res = tmp
        for j in range(i+1, len(l)):
            tmp += l[j]
            if tmp > res:
                res = tmp
        if res > ma:
            ma = res
    return ma

print(maxSubsequeSum_1([-1,-2,-3,4,5,6,-1]))
'''
Output result：
    15
'''

def maxSubsequeSum_2(l):
    if len(l) == 0:
        return 0
    pre = l[0]  #定义上一个元素
    maxList = [pre]  #定义最大值列表
    for i in range(1, len(l)):
        #当前最大元素
        m = max(l[i], l[i] + pre)
        pre = m
        maxList.append(m)
    return max(maxList)

print(maxSubsequeSum_2([-1,2,-3,4,5,6,-1]))
'''
Output result：
    15
'''
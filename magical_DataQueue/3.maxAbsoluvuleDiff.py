#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
3、绝对值最大的两数之差
    现在输入一个二维列表，列表中每一个元素都是一个子列表，子列表中存放的全部是整数，要求通过编程找到所有整数中两数
之差的绝对值最大是多少。例如：输入[[1,2,3], [1,4,5]]，则最终返回结果4，因为这些数中绝对值最大的情况为第一个子列表
的元素1和第二个子列表的元素2，做差值计算。注意：所选择的两个做差计算的元素不能来自同一个列表。
解题方法：
（1）两层循环遍历；
（2）程序优化：只需一层遍历，找到列表中的最值和次最值进行遍历
'''

#两层循环遍历
def maxAbsolue_1(l):
    res = 0
    #循环遍历取出子列表
    for i in l:
        ma = max(i)
        mi = min(i)
        #取出子列表元素
        for j in l:
            #排除两元素来自同一个子列表情况
            if i == j:
                continue
            #不是同一个子列表的最值
            ma2 = max(j)
            mi2 = min(j)
            n = abs(ma2 - mi)
            m = abs(mi2 - ma)
            if max(m, n) > res:
                res = max(m, n)
    return res

print(maxAbsolue_1([[1,2,3], [1,4,5], [0]]))
'''
Output result：
    5
'''

#程序优化
def maxAbsolue_2(l):
    res = 0
    #定义最值
    ma1 = max(l[0])
    mi1 = min(l[0])
    #定义次最值
    ma2 = max(l[0])
    mi2 = min(l[0])
    isOneGroup = True   #最值是否来自同一组元素标记
    #次最值是否有效标记
    isRealMa2 = False
    isRealMi2 = False

    for index in range(1, len(l)):
        item = l[index]
        ma = max(item)
        mi = min(item)
        #ma1和mi1在同一个子列表中
        if ma > ma1 and mi < mi1:
            isOneGroup = True
            ma1 = ma
            mi1 = mi
            continue
        #ma为最大值
        if ma > ma1:
            ma2 = ma1
            ma1 = ma
            isRealMa2 = True
            isOneGroup = False
        #找到最值，跳出循环
        elif ma > ma2 or not isRealMa2:
            ma2 = ma
            isRealMa2 = True
        #mi为最小值
        if mi < mi1:
            mi2 = mi1
            mi1 = mi
            isRealMi2 = True
            isOneGroup = False
        elif mi < mi2 or not isRealMi2:
            mi2 = mi
            isRealMi2 = True
    #如果不是在同一个组中
    if not isOneGroup:
        return abs(ma1 - mi2)
    else:
        return max(abs(ma1 - mi2), abs(ma2 - mi1))

print(maxAbsolue_2([[1,2,3], [0,4,5], [1]]))
'''
Output result：
    4
'''
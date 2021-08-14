#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
13、有序列表判断
    输入一个整数列表，要求编程判断此列表是否是一个有序列表。有序是指列表是递增的或递减的。例如输入列表L为：
[1,2,3,4,5]，返回结果True；输入列表为[5,4,3,2]，也返回结果True。元素列表全递增、全递减或者列表元素全部一样，
都认为是有序列表。
解题思路：
（1）定义一个变量记录当前列表是递增、递减或尚未判定；
（2）依次遍历列表中的元素与上一个元素做对比，判定是否符合预期的递增或递减规则；
（3）如果遍历完整个列表后，没有不符合预期的元素出现，则表明列表是有序的，遍历过程中，如果有一个元素不符合预期，
则表明列表是无序的。
'''

def isOrderList(L):
    #只有两个元素一定是有序的
    if len(L) < 3:
        return True
    tip = 0  #标记
    #递增标记
    if L[1] > L[0]:
        tip = 1
    # 递减标记
    if L[1] < L[0]:
        tip = -1
    for i in range(2, len(L)):
        item1 = L[i-1]
        item2 = L[i]
        if tip == 0:
            #递增判断
            if item2 - item1 > 0:
                tip = 1
            # 递减判断
            elif item2 - item1 < 0:
                tip = -1
            else:
                continue
        #是否符合递增或递减预期条件
        if item2 - item1 >= 0 and tip > 0:
            continue
        elif item2 - item1 <= 0 and tip <0:
            continue
        return False
    return True

print(isOrderList([5,4,3,3,2,2,1]))
'''
Output result：
    True
'''
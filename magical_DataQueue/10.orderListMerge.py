#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
10、递增列表的合并
    现在输入两个列表，列表中的元素都是整数，并且在每个独立的列表中，元素都是递增的，要求编写程序将这两个列表合并
为一个递增列表。例如：输入的两个列表为：[1,3,7]和[2,5,10]，需要合并为[1,2,3,5,7,10]输出。
解题思路：
（1）确定新列表的长度，通过循环来对列表进行元素填充；
（2）使用两个指针变量记录输入的两个列表当前的取值位置；
（3）每次循环，都根据指针的位置从两个输入列表中取元素，并做比较逻辑，将合适的插入新列表，然后通过移动指针来将
新列表填充完毕。
'''

def orderListMerge_1(l1, l2):
    c = len(l1) + len(l2)  #列表总长度
    res = []
    m = 0  #l1指针
    n = 0  #l2指针
    for i in range(c):
        it1 = None
        it2 = None
        if m < len(l1):
            it1 = l1[m]
        if n < len(l2):
            it2 = l2[n]
        if it1 == None:
            res.append(it2)
            n += 1
        elif it2 == None:
            res.append(it1)
            m += 1
        else:
            if it1 >= it2:
                res.append(it2)
                n += 1
            else:
                res.append(it1)
                m += 1
    return res

print(orderListMerge_1([1,3,7],[2,5,10]))
'''
Output result：
    [1, 2, 3, 5, 7, 10]
'''

#程序优化：使用sort()方法将新列表直接进行排序
def orderListMerge_2(l1, l2):
    l = l1 + l2
    l.sort()
    return l

print(orderListMerge_2([1,3,7],[2,5,10]))
'''
Output result：
    [1, 2, 3, 5, 7, 10]
'''
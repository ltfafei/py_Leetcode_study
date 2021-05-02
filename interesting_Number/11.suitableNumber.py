#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
11、定义顺次数为其每一位数字都比前一位数字大1的整数。例如123, 234, 345, 456等都是顺次数。
    现在，给定一个范围,例如[1000, 10000)，尝试编程查找其范围内的所有顺次数，并将其从小到大的组成列表返回。

解题思路：
    由于每一位比前一位大1，那最小是1，最大就是9。
'''

def suitableNumber(low, high):
    l = []
    #获取第一位，先从大到小排序，如：321，获取到第一位是1
    for num in range(1, 10):
        #获取从又到左前两位，根据如上就是：21，依次循环
        for j in range(num+1, 10):
            num = num * 10 + j
            if num <= high and num >= low:
                l.append(num)
    #从左往右，从小到大排序
    l.sort()
    return l
print(suitableNumber(1000, 10000))


'''
Output result：
    [1234, 2345, 3456, 4567, 5678, 6789]
'''
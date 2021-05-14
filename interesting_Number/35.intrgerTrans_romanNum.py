#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
35、整数转罗马数字
    现在要求通过编程实现输入一个1-3999的数字，将其转换为罗马数字输出。
'''

def integerTrans_rman(num):
    #做好个十白千位与罗马数字的映射，0使用空字符串表示
    l1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    l2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    l3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    l4 = ["", "M", "MM", "MMM"]

    l = [l1, l2, l3, l4]
    i = 0
    res = ""
    #大于10的数的判断
    while (int(num / 10) > 0) or ((num % 10) > 0):
        tl = l[i]
        i += 1
        tmp = num % 10
        num = int(num / 10)
        res = tl[tmp] + res
    return res

print(integerTrans_rman(3999))
'''
Output result：
    MMMCMXCIX
'''
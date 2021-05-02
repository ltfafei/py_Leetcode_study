#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
16、首先，累加数是一个字符串，至少包含3位数，除了最开始的两个数外（最开始的两个数不能为0），字符串中的其他数
都等于它之前两个数相加的和。
    例1：’112358‘是一个累加数，因为拆解后：
        1 + 1 = 2
        1 + 2 = 3
        2 + 3 = 5
        3 + 5 = 8
    例2：’58132134‘是一个累加数，因为拆解后：
        5 + 8 = 13
        8 + 13 = 21
        13 + 21 = 34
    现在，输入一个字符串类型的数，通过编程判断其是否是一个累加数。

解题思路：
    本题看似简单，实际暗藏玄机。为什么这么说呢？如果每次获取的第一个数和第二个数都是一位数
还简单，就像上面的例1；但如果变成了两位数甚至三位数，如何进行判断？如例2。所以本题的难点在于
如何确定第一个数和第二个数。只要确定了第一个数和第二个数，则后面的数都可以通过前面两个数累加来
验证，因此，需要通过嵌套循坏的方式来穷举第一个数与第二个数的组合情况，再通过累加数特性来验证。
'''

def func(end1, end2, num):
    res = num[0: end2+1]   #截取第一位数和第二位数
    c1 = num[0: end1+1]    #取出第一个数
    c2 = num[end1+1: end2+1]    #取出第二个数
    if res == num:
        return False
    #剔除第一个数和第二个数为0的情况
    if (len(c1) > 1 and c1[0] == "0" or (len(c2) > 1 and c2[0] == "0")):
        return False
    #可以进行累加的情况
    while len(res) < len(num):
        c3 = str(int(c1) + int(c2))
        res += c3
        c1 = c2
        c2 = c3
    if res == num:
        return True
    return False

def summation_num_Check(num):
    if len(num) < 3:
        return  False
    for i in range(0, len(num) - 1):
        for j in range(i+1, len(num)):
            if func(i, j, num):
                return  True
    return False

print(summation_num_Check('167132033'))
print(summation_num_Check('1000'))

'''
Output result：
    True
    False
'''
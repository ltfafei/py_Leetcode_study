#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
26、实现平方根函数
    在python中，导入math库，可以使用math.sqrt()方法很轻松求个某个数的开方结果。
现在，要求不使用math库，通过编程实现输入一个正整数，求它的开方结果。

解题思路：
（1）二分法；
（2）向下取整。
'''

import math

def get_Square(num):
    l = 0   #标记从0开始
    r = num   #标记从num开始
    while l < r:
        s = int(l + r) / 2  #二分
        #正好开方的情况
        if s * s == num:
            return s
        #位于右边界情况
        elif s * s < num:
            l = s + 1
        else:
            r = s - 1
    #左右边界判断开方
    if l * l > num:
        return  int(l - 1)
    else:
        return int(l)

print(get_Square(9))
print(math.sqrt(9))

'''
Output result：
    3.0
    3.0
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
27、平方数之和
    假设给定一个非负整数N，要求通过编程判断是否存在两个整数A和B，使得
A的平方加上B的平方的和等于N。

解题思路：
（1）遍历—如果N不大时，可使用将A和B进行遍历的方法；
（2）夹逼：如果N很大时，两个数的平方也会很大，所以可以采用从两边往中间夹逼的方法。
'''

#夹逼法
import math
def square_numSum(N):
    l = 0   #标记下边界
    r = int(math.sqrt(N))   #标记上边界
    while l <= r:
        res = l * l + r * r
        if res < N:
            l = l + 1   #左边界+1
        elif res > N:
            l = l - 1   #右边界-1
        else:
            print(l)
            print(r)
            return True
    return False

print(square_numSum(5))

'''
Output result：
    1
    2
    True
'''
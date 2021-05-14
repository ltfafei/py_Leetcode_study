#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
30、二进制中1的个数
    现在给定两个整数L和R，分别表示范围的左边界和右边界。在这个范围内，如果一个数值的二进制表示
中1的个数是质数，则将其标记为一个特殊数，要求通过编程返回范围内所有特殊数的个数。
'''

#判断质数
import math
def isPrime(n):
    i = 2   #从2开始，1本身不是质数
    while i <= int(math.sqrt(n)):    #如果小于n的开方，说明不是质数
        if n % i == 0:
            return False
        i += 1
    if n >= 2:
        return True
    return False

#通过二进制结合位运算计算
def count_bin1Sum1(L, R):
    res = 0
    for i in range(L, R+1):
        n = i
        c = 0   #标记1的个数
        while n > 0:
            c += n & 1
            n = n >> 1  #右移剔除最后一位
        if isPrime(c):
            res += 1
    return  res

print(count_bin1Sum1(2, 5))
print(bin(2)[2:])
print(bin(3)[2:])
print(bin(4)[2:])
print(bin(5)[2:])

'''
Output result：
    2
    10
    11
    100
    101
'''

#通过内置bin()方法优化
def count_bin1Sum2(L, R):
    res = 0
    for i in range(L, R+1):
        str = bin(i)
        c = str.count("1")  #统计1的个数
        if isPrime(c):
            res += 1
    return  res

print(count_bin1Sum2(2, 5))
'''
Output result：
    2
'''
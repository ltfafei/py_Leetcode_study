#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
3、完全平方数有这样的特性：如果一个正整数A是某一个整数B的平方，那么这个正整数A叫做完全平方数，零也可称为完全平方数。
    那么：给定正整数N，找到若干个完全平方数使得它们的和等于N，你需要确定组成和的完全平方数的最少的个数。
    例如：对于正整数13，其可以拆解为13=4+9，则最少个数为2；对于正整数12，其可以拆解为12=4+4+4，则最少个数为3.

解题需用到：四平方数和定理
    四平方数和定理又称拉格朗日四平方数和定理，由拉格朗日最终解决。
    四平方数和定理可以证明：任何正整数均可表示为四个整数的平方和(其中允许有整数为0)。
    根据四平方数和定理：
        13 = 4 + 9 + 0 + 0
        12 = 4 + 4 + 4 + 0
    从该定理可知：组成这个正整数N的完全平方数的个数最多为4个。
    四平方数和定理推论：
        如果一个数N只能使用4个非零的完全平方数的和表示，则这个数N一定满足：4^A(8B+7)

解题算法思路：
（1）先假设组成这个数N的完全平方数的个数最少为4，则数N必定满足：N=4^A(8B+7)，
先对这个等式进行判断，如果通过，则最终答案为4，否则继续算法；
（2）假设组成这个数N的完全平方数的个数最少为1，则数N可以表示为某个正整数的平方，
进行遍历，如果找不到继续算法；
（3）假设组成这个数N的完全平方数的个数最少为2，使用循环嵌套进行遍历，找不到继续算法；
（4）算法执行到此，则最终答案为3。
'''

def entireSquareNumber(N):
    num = N
    #判断是否是4的倍数
    while num % 4 == 0:
    #判断是否满足：4^A(8B+7)
        num = num / 4
    if num % 8 == 7:
        return 4
    for i in range(1, N+1):
        if i * i == N:
            return 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i * i + j * j == N:
                return 2
    return 3
print(entireSquareNumber(100))

'''
Output result：
    1
'''

'''
    如果给定的N数值很大，由于经过多次循环和幂运算，导致程序很慢。
'''
#程序优化

import math

def entireSquareNumber2(N):
    num = N
    while num % 4 == 0:
        num = num / 4
    if num % 8 == 7:
        return 4
    #导入math库，math.sqrt()开方运算，math.pow()幂运算
    if math.pow(int(math.sqrt(N)), 2) == N:
        return 1
    max = int(math.sqrt(N)) + 1
    for i in range(1, max):
        tmp = N - i * i
        if math.pow(int(math.sqrt(tmp)), 2) == tmp:
            return 2
    return 3

print(entireSquareNumber2(7000))

'''
Output result：
    3
'''
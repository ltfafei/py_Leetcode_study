#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
7.1、判断丑数
    丑数是指只包含质因数2、3、5的正整数。
质因数：
    质数是指一个整数的因数只有1和它本身而没有其他的因数，这样的数叫做质数（或素数）。
一个合数的因数是质数，这个因数叫做这个合数的质因数。

    现在，输入一个正整数，判断其是否为丑数。
解题思路：
    方法1：将小于所输入数的所有质数寻找出来，然后依次验证是否可以整除。
    方法2：将输入的数循环对2、3、5这三个数进行整除操作，直到最终无法整除2、3和5，
    这时，如果余数为1，则说明还存在其他的质因数。
'''

def uglyNumber(N):
    if N <= 0:
        return False
    # 1本身就是质因数
    if N == 1:
        return True
    #判断N大于等于2的情况
    while N >= 2:
        if N % 2 == 0:
            N = N / 2
            continue
        if N % 3 == 0:
            N = N / 3
            continue
        if N % 5 == 0:
            N = N / 5
            continue
        break
    if N == 1:
        return True
    return False
print(uglyNumber(12))

'''
Output result：
    True
'''

#7.1 程序优化

def uglyNumber2(N):
    #直接将2，3，5放到元组中进行判断
    for i in (2, 3, 5):
        while N % i == 0:
            N = N / i
    if N == 1:
        return True
    return False
print(uglyNumber2(11))

'''
Output result：
    False
'''

'''
7.2、寻找丑数
    如果将丑数按照自然数的顺序来进行排序的话，正整数1是第一个丑数，
    现在输入一个数N，尝试使用编程找到第N个丑数
'''

def uglyNumber3(N):
    num = 1
    i = 1
    while num < N:
        i += 1
        if uglyNumber2(i):
            num += 1
    return i
print(uglyNumber3(500))

'''
Output result：
    937500
'''

'''
    当输入的数很大的话，程序会运行很慢
7.2 程序优化
（1）首先定义一个数组，用来存放所有已经找到的丑数；
（2）使用3个变量分别用来记录对因数2、3和5相乘运算的位置；
（3）将找到的最小丑数放入数组，修改记录位置的变量，继续寻找，知道满足要求。
'''

def uglyNumber4(N):
    l = [1]  #[1, 2, 3]
    p2 = 0
    p3 = 0
    p5 = 0
    while len(l) < N:
        #找到最小的丑数
        minN = min(l[p2] * 2, l[p3] * 3, l[p5] * 5)
        l.append(minN)
        if l[p2] * 2 == minN:
            p2 += 1
        if l[p3] * 3== minN:
            p3 += 1
        if l[p5] * 5 == minN:
            p5 += 1
    return l.pop()
print(uglyNumber4(500))

'''
Output result：
    937500
'''
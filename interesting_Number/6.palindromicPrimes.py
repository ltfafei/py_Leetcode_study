#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
6、前面回文数的问题比较简单，这次来求回文素数。素数是指大于1且因数只有1和它本身的数。
回文素数既满足素数的特点也满足回文数的特点。

    现在，输入一个数N，要求求出大于或等于数N的最小回文素数，使用编程实现。
'''

import math

def checkPalindromic(N):
    return str(N) == str(N)[::-1]

def checkPrimes(N):
    # 1不是素数，排除N=1的情况
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N) + 1)):
    # 可以与i整除的数，说明不是素数
        if N % i == 0:
            return False
    return True
#print(checkPrimes(373))

def getminPaliprimes(N):
    while True:
        if checkPalindromic(N):
            if checkPrimes(N):
                return N
        N += 1

print(getminPaliprimes(7000))

'''
Output result：
    10301
'''

'''
程序优化：
    当输入的N很大时，由于需要循环进行判断，会导致程序很慢甚至卡死。
回文数和素数特点：
    （1）除11以外的偶数位回文数，都能被11整除；
    （2）除了2和3以外，其他所有的素数对6取余一定等于5或者等于1。
优化方式：
    由上面的第1条数学规律，除了数字11外，在暴力尝试时我们可以将所有的偶数位数的数值剔除掉。
    由上面第2条规律，我们可以在素数验证前先通过取模运算进行一轮筛选，并且暴力尝试的步长也可以根据取模运算的结果做调整。
'''

def getminPaliprimes2(N):
    while True:
        string = str(N)
        #除11外，将所有偶数位剔除掉
        if N > 11 and len(string) % 2 == 0:
            new_string = ""
            for i in range(0, len(string)):
                new_string = new_string + "0"
            new_string = "1" + new_string
            N = int(new_string) + 1
            continue
        tmp = 0
        if N > 3:
            tmp = N % 6
        #取余不等于1并且不等于5，说明不是素数
        if tmp > 0 and tmp != 1 and tmp != 5:
            continue
        if checkPalindromic(N):
            if checkPrimes(N):
                return N
        #控制步长
        if tmp == 1:
            N = N + 4
        elif tmp == 5:
            N = N + 2
        else:
            N = N + 1

print(getminPaliprimes2(7000))

'''
Output result：
    10301
'''
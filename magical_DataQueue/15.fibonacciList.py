#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
15、斐波那契数列
    在斐波那契数列中，第一个元素为0，第二个元素为1，之后的每个元素都是前两个元素之和。例如：
[0,1,1,2,3,5,8,13]就是一个斐波那契数列。现在输入一个整数N，其表示斐波那契列表中下标为N的元素，
要求编程将这个元素推到出来。例如输入N=6，则需要返回元素8作为答案。
解题方法：
（1）递归：斐波那契数列本身就是一个递归的过程；
（2）循环：循环遍历找到下标为N的元素。
'''

#递归
def fibonacciList_1(N):
    #定义递归函数
    def func(index):
        #对斐波那契数列前两个元素进行特殊处理
        if index == 0:
            return 0
        elif index == 1:
            return 1
        else:
            #进行递归推到
            return func(index-1) + func(index-2)
    return func(N)

print(fibonacciList_1(6))
'''
Output result：
    8
'''

#循环遍历
def fibonacciList_2(N):
    #前两个元素下标处理
    if N == 0:
        return 0
    if N == 1:
        return 1
    #定义前两个元素
    a = 0
    b = 1
    #循环遍历元素
    for i in range(2, N+1):
        c = a+b
        a = b
        b = c
    return b

print(fibonacciList_2(7))
'''
Output result：
    13
'''
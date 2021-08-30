#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
9、宝石鉴定
    现在，输入一个字符串J表示样品列表，其中每一个字符都表示一种类型的宝石，且没有重复的字符存在
（区分大小写）。再输入一个需要鉴定的列表S，现在需要编程鉴定出宝石的数量并返回。
例如：输入J为ab，S为：acbAFei，则需要返回宝石数量为2。
'''

def isGem(J, S):
    c = 0  #记录宝石的数量
    #通过遍历筛选宝石
    for i in S:
        if i in J:
            c += 1
    return c

print(isGem(["a", "b"], ["a", "c", "b", "A", "f", "E", "i"]))
'''
Output result：
    2
'''
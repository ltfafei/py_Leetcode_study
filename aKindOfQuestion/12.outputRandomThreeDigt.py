#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
12、输出随机三位数
    现在输入一个整数范围x-y，要求编程输出随机三位数。
'''

def outputRanThree(x, y):
    for i in range(x, y):
        for j in range(x, y):
            for k in range(x, y):
                # 保证数字不会重复
                if (i != j) and (i != k) and (j != k):
                    return "输出的三位数是：%d%d%d" % (i, j, k)
    return "无法构成三位数！"

print(outputRanThree(2, 6))
'''
Output result：
    输出的三位数是：234
'''
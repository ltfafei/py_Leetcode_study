#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
32、整数转换十六进制数
    现在给定一个数，要求通过编程将其转换为十六进制数。注意：转换的结果中不能包含多余的前置0
(数0本身除外)，输入的数字为32为有符号数，并且如果输入的是负数，需要以补码的方式输出。例如：
输入-1，那么结果输出为：FFFFFFFF
'''

#十六进制和位运算解题
def integerTransHex(n):
    n = n & 0xffffffff
    #建立下标与十六进制的映射关系
    l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    res = ""
    while n > 0:
        tmp = n & 0xf   #从右向左取出4位
        res = l[tmp] + res
        n = n >> 4
    #数值0返回0
    if res == "":
        res = "0"
    return res

print(integerTransHex(-1))
'''
Output result：
    ffffffff
'''
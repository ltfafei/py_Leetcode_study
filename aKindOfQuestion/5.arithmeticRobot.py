#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
5、算术机器人
    现在利用编程设计一个简单的算术机器人，只需输入两个数字，在输入一个指令，机器人可计算并将结果返回。
输入的数值可以是任意整数，假设为X和Y，计算指令为A和B。A指令进行如下运算：
X*2+Y
Y指令表示如下运算：
Y*2+X
如果输入指令：AB，则先进行A指令运算，再进行B指令运算。最终将运算结果返回。
'''

def arithRobot(x, y, s):
    n = 0
    for c in s:
        if c == "A":
            n += 2 * x + y
        else:
            n += 2 * y + x
    return n

print(arithRobot(3, 9, "AB"))
'''
Output result：
    36
'''
#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
28、删除重复相邻字符（栈结构解题）
    现在输入一个字符串，要求编程实现将字符串中相邻且相同的字符删除，如果删除之后组成的字符串中依然存在
相邻且相同的字符，继续递归删除，直到字符串中不存在相邻且相同的字符串为止。例如：输入字符串：AFEIIEO，
需要返回结果：AFO。
'''

def delReAdjacentStr(s):
    stack = []
    #遍历字符串
    for i in s:
        #如果栈中有元素并且当前元素为栈顶元素
        if len(stack) > 0 and i == stack[-1]:
            stack.pop()  #出栈
        #否则入栈
        else:
            stack.append(i)
    return "".join(stack)

print(delReAdjacentStr("AFEIIEO"))
'''
Output result：
    AFO
'''
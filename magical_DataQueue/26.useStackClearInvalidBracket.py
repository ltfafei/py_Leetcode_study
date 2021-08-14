#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
26.1、利用栈清理无效括号
    现在输入一个字符串，字符串由26个字母与括号字符"("和")"组成。一个有效的字符串中，括号必须成对出现，
但是输入的字符串并不一定是有效的，现在要求使用栈这种数据结构，删除最少的括号字符，使其变成有效的字符串
输出。例如输入：)AF(ei)(a(fei))one)，则需要返回：AF(ei)(a(fei))one
解题思路：
（1）定义一个栈容器来存储数据；
（2）对输入的字符串进行遍历，如果遇到左括号"("，直接入栈，需要记录入栈元素的字符和位置；
（3）如果遇到右括号")"，检查栈顶的元素是否是左括号，如果是，直接出栈，不是则将当前右括号元素入栈；
（4）当整个字符串遍历结束后，检查栈中是否有元素，依次将原字符串中栈元素对应位置字符删除。
'''

def clearInvlidBracket(s):
    #入栈初始化方法
    class StackItem:
        def __init__(self, index, char):
            self.index = index
            self.char = char
    stack = []  #定义栈列表
    #遍历字符串，处理括号
    for i in range(len(s)):
        c = s[i]
        #如果是左括号，入栈
        if c == "(":
            item = StackItem(i, c)
            stack.append(item)
        #如果是右括号，出栈
        elif c == ")":
            if len(stack) > 0 and stack[-1].char == "(":
                stack.pop()
            else:
                item = StackItem(i, c)
                stack.append(item)
    #从后往前删除
    while len(stack) > 0:
        item = stack.pop()
        #取出最后一个元素
        s = s[:item.index] + s[item.index+1:]
    return s

print(clearInvlidBracket(")AF(ei)(a(fei))one)"))
'''
Output result：
    AF(ei)(a(fei))one
'''

'''
26.2、处理平衡括号
    现在定义，一对平衡括号为左右对称的一对小括号"()"，一对纯粹的平衡括号定义其分值为1，嵌套
的平衡括号分值会被翻倍。例如："(()())"的分值为4。现在输入一个有效的平衡括号字符串。要求编程
统计其分值。
解题思路：利用栈思路解题
（1）创建一个栈容器来处理括号的逻辑，对输入的字符串进行遍历，如果遇到"("，则直接进入栈中；
（2）如果遇到")"，则需要找到栈中之前的"("元素与其匹配，将匹配到的"("字符与其后所有元素都
进行出栈操作，并将匹配到的小括号的分值进行乘2操作(如果为空，则默认分值为1)，将数值进行入栈。
（3）将栈中余下的所有分值进行累加，即得到最终的答案。
'''

def countBracket(s):
    stack = []  #定义栈容器
    #遍历字符串
    for i in range(len(s)):
        char = s[i]
        #如果为"("，直接入栈
        if char == "(":
            stack.append(char)
        #进行分值计算
        if char == ")":
            t = 0
            while stack[-1] != "(":
                t = t + stack[-1]
                stack.pop()
            stack.pop()
            # if t == 0:
            #     t = 1
            # else:
            #     t = t * 2
            #如果分值为0，则表明是最内层括号，将分值修订为1
            stack.append(1 if t == 0 else t * 2)
    #小括号计数
    res = 0
    for i in stack:
        res += i
    return res

print(countBracket("((af)(ei))"))
'''
Output result：
    4
'''
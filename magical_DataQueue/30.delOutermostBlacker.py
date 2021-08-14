#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
30、删除最外层括号
    输入一个只包含小括号的字符串，字符串中的括号都是成对出现的，并且括号可能存在嵌套，要求编程将最外层
的括号删除。最外层可能存在多个并列括号对，那就需要将其都删掉。例如输入：(())(())，则返回：()()作为结果
解题思路：
（1）定义一个栈容器，标记变量和结果字符串变量，并对输入的字符串进行遍历。
（2）遍历过程中，如果遇到左括号，则进行逻辑判定，如果当前在外层括号内，则进行入栈，并将字符追加到结果
字符串中。如果当前不再外层括号内，则将标记变量设置为True；
（3）遍历过程中，如果遇到右括号，则进行逻辑判定，如果当前在外层括号内，则检查栈中是否有元素，有则将
栈顶元素出栈，并追加当前字符到结果字符串中，否则将标记变量设置为False。遍历完成后，将结果字符串返回
即可。
'''

def delOutermmostBlacker(s):
    stack = []
    tip = False  #标记变量
    res = ""  #结果字符串
    for i in s:
        if i == "(":
            #遇到左括号，说明在内层，进行入栈操作
            if tip:
                stack.append(i)
                res += i
            else:
                tip = True
        #遇到右括号
        else:
            if tip:
                if len(stack) > 0:
                    stack.pop()
                    res += i
                else:
                    tip = False
    return res

print(delOutermmostBlacker("(())(()())"))
'''
Output result：
    ()()()
'''
#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
27、括号内容逆序
    现在输入一个字符串，字符串中只包含英文字母与小括号字符”()“，小括号的作用是：对括号内的内容进行
逆序，小括号可以嵌套。如果有嵌套产生，则优先处理内部括号，再处理外部括号。
例如：输入一个字符串为：(I((EFA)(OLL)HE))，则首先处理最内层括号：(I(AFELLOHE))，再处理第二层括号：
(IEHOLLEFA)，再处理最外层括号，得到最终结果：AFELLOHEI。
解题思路：
（1）首先创建一个栈容器，对输入的字符串进行遍历，并将遍历出的字符串进行入栈；
（2）当遇到右括号")"时，将栈顶到最近的一个左括号之间的元素进行出栈，逆序后，再将字符重新入栈；
（3）遍历完一轮以后，将栈中的字符拼接成字符串返回即可。
'''

def brackContentReverse(s):
    stack = []  #定义栈结构
    #对字符串进行遍历
    for i in s:
        #遇到右括号时
        if i == ")":
            l = []
            #将与之匹配的栈顶最近的左括号内容出栈，逆序拼接
            while stack[-1] != "(":
                l.append(stack.pop())
            #将对应的左括号进行出栈
            stack.pop()
            stack += l
        #非右括号直接入栈
        else:
            stack.append(i)
    return "".join(stack)

print(brackContentReverse("(I((EFA)(OLL)HE))"))
'''
Output result：
    AFO
'''
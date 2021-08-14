#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
31、简化文件路径
    在计算机中，文件路径表示方式如下：/User/Afei/demo.py，这种路径表示方式是最简洁的。其中最前面的/表示
根目录，不加/表示当前目录，还有./表示当前目录，../表示上级目录。例如：
/User/Afei/demo.py
/User/Afei/./demo.py
/User/Afei/Python/../demo.py
上面三种路径表述方式是一至的。现在，输入一个路径字符串，要求通过编程将其进行简化。输入路径中可能包含
"."、".."和冗余的"/"（连续出现的/或在非根目录的结尾出现的/），例如输入：/User//Afei/../demo.py/./
需要返回结果：/User/demo.py作为答案。
解题思路：
（1）将连续的斜杠字符"/"进行清理；
（2）将容器的当前目录符号"."进行清理；
（3）将上层目录符号".."进行简化，如果其指定的上层目录不是根目录，则将其进行清理。
'''

def simplifyFilePath(path):
    #原始栈，存放解析出的原始目录
    stack = []
    tmp = ""  #临时变量，记录当前解析出的元素
    #将目录解析出来放入原始栈中
    for i in path:
        if i == "/":
            stack.append(tmp)
            tmp = ""
        else:
            tmp += i
    stack.append(tmp)
    res = []  #定义结果栈
    stack = stack[::-1]  #对原始栈进行逆序，从前往后遍历
    while len(stack) > 0:
        item = stack.pop()
        #空元素情况，说明之前处理了重复的斜杠字符，直接跳过
        if item == "":
            continue
        #当前目录，直接跳过
        if item == ".":
            continue
        #上层目录，如果结果栈中有元素，则栈顶元素出栈
        if item == "..":
            if len(res) > 0:
                res.pop()
            continue
        res.append(item)
    #将最终结果拼接成字符串返回
    newStr = "/" + "/".join(res)
    return newStr

print(simplifyFilePath("/User//Afei/../demo.py/./"))
'''
Output result：
    /User/demo.py
'''
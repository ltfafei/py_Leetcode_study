#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
29、实现条件运算符
    在python中，条件运算符描述如下：
X = 1 IF CONDITION ELSE 0
上面表达式含义是：如果CONDITION表达式的值为True，则变量X赋值为1，否则赋值为0。但在其他编程语言中，
条件表达式也有其他描述方法，如：
X = CONDITION ? 1 : 0
以上其实是三元运算符，表示含义与第一个表达式一致。注意：条件表达式也可以嵌套使用，且运算时是右
结合性的。例如：X1 ? 0 : X2 ? 1 : 2可以表示为 X1 ? 0 : (X2 ? 1 : 2)。现在要求使用python实现问好
冒号形式的条件运算符。
解题思路（栈结构解题）：
（1）定义栈容器和一个标记变量tip，tip变量的作用是标记下一次遍历出的字符是否是条件判定字符。由于条件
运算符是右结合性的，因此需要逆向对输入的字符串进行遍历。
（2）在遍历过程中，遇到字符:则直接跳过，遇到字符?则进行tip变量标记，表明它的下一个字符为条件判定字符；
（3）在遍历过程中，如果不是上述情况，则进行逻辑判定，如果tip变量没有被标记，则直接入栈；如果tip变量
被标记，则判断当前字符是T还是F，如果为T，则保留栈顶元素，并删除栈顶后的第一个元素，如果是
F，则删除栈顶元素。遍历完成后，栈顶元素既是最终答案。
'''

def theCondition(s):
    stack = []
    tip = 0  #标记变量
    #逆向遍历
    for i in s[::-1]:
        if i == ":":
            continue
        #标记下次遍历的字符为条件判定字符
        elif i == "?":  #遍历到条件表达式
            tip = 1
        else:
            if tip == 1:
                #栈顶元素为当前子条件的值
                if i == "T":
                    t = stack.pop()
                    stack.pop()
                    stack.append(t)
                #栈顶元素后的第一个元素为当前条件的值
                else:
                    stack.pop() #栈顶元素出栈
            else:
                stack.append(i)
            tip = 0
    return stack.pop()

print(theCondition("T?F?1:2:0"))
'''
Output result：
    2
'''
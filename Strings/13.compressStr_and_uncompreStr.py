#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
13.1、压缩字符串
    在网络传输时，对字符串进行压缩可以非常客观的减少网络交互的数据量。加快网络传输速度，减少用户流量的消耗。
在进行大量字符串类型的数据传输时，对字符串进行压缩是不可避免的。
    现在将字符串中连续重复的字符进行压缩。如果压缩后的字符串比原字符串短，则返回压缩后的字符串；如果压缩后的
字符串不比原字符串短，则返回原字符串。
压缩规则如下：
    将字符与其出现的次数组合来压缩字符串。例如：输入字符串AABBCCCCD，压缩后返回A2B2C4D1，压缩后的字符串比原来
的字符串短，所以返回结果：A2B2C4D1
'''

def compressStr(s):
    res = ""        #压缩结果
    curreChar = ""  #当前重复字符
    curCount = 0    #当前字符出现字符
    for c in s:
        if len(curreChar) > 0:
            #当前字符等于重复字符，进行计数
            if c == curreChar:
                curCount += 1
            else:
                res += curreChar
                res += str(curCount)
                curreChar = c
                curCount = 1
        else:
            curreChar = c
            curCount = 1
    res += curreChar
    res += str(curCount)
    #结果字符串和输入字符串长度判断
    if len(res) >= len(s):
        return s
    else:
        return res

print(compressStr("AABBCCCCD"))
'''
Output result：
    A2B2C4D1
'''

'''
13.2、解压字符串
    字符串解压是对字符串压缩的一种逆运算。现在规定输入一个经过压缩后的字符串，需要通过编程将其还原成
原字符串。解压规则如下：
K[str]
其中str代表要展开的字符，K代表要展开的次数。例如：输入：3[a]1[f]2[e]3[i]，解压得到：aaafeeiii，输入
2[a3[c]]，解压得到：acccaccc

难点：
    对于字符串的解压是可以嵌套的，可以使用递归函数来解决。但是遇到数字和中括号这类特殊字符时，需要做
特殊的逻辑处理。
解题算法：
（1）首先定义变量：res存放最终结果，deep记录递归深度，count记录当前字符串需要展开的次数，chars记录
需要递归运算的子串。
（2）对输入字符串进行遍历操作；
（3）当遇到"["字符串时，表明需要进行递归操作，并将当前递归深度deep加一；当遇到"]"字符时，表明嵌套逻辑
的闭合，将当前递归深度减一；当遇到"]"字符且递归深度变为0时，进行递归运算；
（4）当遇到数字字符时，如果当前递归深度为0，则使用count进行记录，否则拼接到chars子串中；
（5）当递归深度deep大于0时，遍历到的当前字符串都需要拼接到chars子串中；当deep等于0时，遇到非特殊字符
直接拼接到res结果字符串中。
'''

def uncompreStr(s):
    res = ""
    deep = 0
    count = ""
    chars = ""
    #展开次数0-9的映射
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for c in s:
        if deep > 0:
            chars += c
        if c in nums and deep == 0:
            count += c
        #当前字符为[，进行递归
        elif c == "[":
            deep += 1
        elif c == "]":
            deep -= 1
            if deep == 0:
                res += uncompreStr(chars) * int(count)
                #制空
                chars = ""
                count = ""
        elif deep == 0:
            res += c
    return res

print(uncompreStr("3[a]1[f]2[e]3[i]"))
'''
Output result：
    aaafeeiii
'''

print(uncompreStr("2[a3[c]]"))
'''
Output result：
    acccaccc
'''
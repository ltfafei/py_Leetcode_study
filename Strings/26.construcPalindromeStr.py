#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
26.1、验证回文字符串
    现在输入一个字符串语句，要求通过编程从字符串角度验证其是否是回文字符串(所有字符均为小写，可以忽略空格)。
例如：输入"room ma am moor"，结果为True
'''

def checkPalindrome(s):
    #定义chars和nums列表来筛选字母和数字字符
    chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
             "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
             "w", "x", "y", "z"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    res = ""
    for c in s:
        c = c.lower()   #字母统一转成小写
        if (c in chars) or (c in nums):
            res += c
    return res == res[::-1]  #判断是否是回文字符串

print(checkPalindrome("room ma am moor"))
'''
Output result：
    True
'''

'''
26.2、构造回文字符串
    现在输入一个字符串，要求通过编程来判断这个字符串是否可以通过重排来构造出回文字符串。例如：输入
字符串为："afeiafei"，则返回结果True。因为可以构造："afeiiefa"，是一个回文字符串。
解题思路：
    首先，如果回文字符串中的字符个数为偶数，则其中所有的字符一定是成对出现的。如果是奇数，则除了一个
字符的个数是奇数外(该字符串放中间)，其他字符的个数也一定是偶数。因此，要判断这些字符能否构成回文字符串，实际上就是对
字符的个数进行统计后判定是否满足奇偶条件。
'''

def constrPalinStr_1(s):
    dic = {}  # 统计单词个数
    #遍历循环统计当前单词出现个数
    for c in s:
        if c in dic.keys():
            dic[c] += 1
        #如果第一次出现，则计数为1
        else:
            dic[c] = 1
    tmp = 0  #奇数个数计数
    for i in dic.items():
        #如果单词个数不是偶数
        if i[1] % 2 != 0:
            tmp += 1
    if tmp > 1:
        return False
    return True

print(constrPalinStr_1("afeiiefaI"))
'''
Output result：
    True
'''

'''
26.3、构造回文字符串进阶
    要求对上面代码进行改造，将其所有可能组成的回文字符串返回。例如：输入"AFAF"，将返回["AFFA", "FAAF"]。
解题思路：
    首先，一组字符如果可以构成回文字符串，除了可以有一个奇数个数的字符外，其他字符一定是成对出现的。
对于回文字符串，如果其前半部分确定了，则后半部分也都确定了。因此，需要做的实际上就是一道全排列的题。
可以使用递归+决策回溯来解决
'''

def constrPalinStr_2(s):
    dic = {}  # 统计单词个数
    for c in s:
        if c in dic.keys():
            dic[c] += 1
        else:
            dic[c] = 1
    tmp = 0  # 奇数个数计数
    c = ""  #记录奇数字符
    for i in dic.items():
        # 如果单词个数不是偶数
        if i[1] % 2 != 0:
            tmp += 1
            c = i[0]
    if tmp > 1:
        return []
    #多个奇数字符处理
    if c != "":
        dic[c] -= 1
    l = []
    #取出左半部分
    for i in dic.items():
        count = int(i[1] / 2)
        for index in range(count):
            l.append(i[0])
    res = []  #记录递归结果
    #递归回溯进行全排列
    def sele(start, li):
        if start >= len(li)-1:
            res.append(li)
            return
        sele(start+1, list(li))
        #循环遍历将字符进行交换
        for index in range(start+1, len(li)):
            #字符交换
            tmpL = list(li)
            tmp = li[start]
            tmpL[start] = tmpL[index]
            tmpL[index] = tmp
            sele(start+1, tmpL)
    sele(0, l)
    l = []
    #将左半部分拼接成回文字符串
    for i in res:
        l.append("".join(i) + c + "".join(i[::-1]))
    return list(set(l))

print(constrPalinStr_2("afeaf"))
'''
Output result：
    ['faeaf', 'afefa']
'''
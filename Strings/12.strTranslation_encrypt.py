#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
12、字符串平移加密
    现在输入一组字符串和一个密钥，这里的密钥指的是字符串平移的次数。要求通过编程写程序来实现字符串
的解密。程序输入三个参数：需要加解密的字符串列表、密钥（次数）、运算模式（布尔型）。例如：输入：
["HELLO", "WORLD"], 3, True，则程序输出：["LOHEL", "LDWOR"]。
'''

#加密
#s：字符串，c：密钥
def enc(s, c):
    res = s
    #平移遍历
    for i in range(0, c):
        res = res[1:] + res[0]
    return res

#解密
def dec(s, c):
    res = s
    for i in range(0, c):
        res = res[-1] + res[:-1]
    return res

def func(l, c, isEnc):
    res = []
    for s in l:
        if isEnc:
            res.append(enc(s, c))
        else:
            res.append(dec(s, c))
    return res

print(func(["HELLO", "WORLD"], 3, True))
'''
Output result：
    ['LOHEL', 'LDWOR']
'''

print(func(["LOHEL", "LDWOR"], 3, False))
'''
Output result：
    ['HELLO', 'WORLD']
'''
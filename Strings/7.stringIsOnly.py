#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
7.1、检查字符串中所有字符是否唯一
    现在输入一个字符串，要求通过编程判断字符串中的所有字符是否全都不同。换句话说：需要判断此字符串中所有
字符是否是唯一的，如果是返回True，如果不是返沪False。例如：输入：word，返沪True。因为字符串word中每个字符
都不相同。
解题思路：
方法一：遍历（遍历字符串中所有字符，如果有相同字符出现则返回False，否则返回True）
方法二：集合去重（利用集合自动去重的特性）
'''

def stringIsOnly_1(string):
    box = set()  #集合存放字符
    for i in  string:
        if i in box:
            return False
        box.add(i)
    return True

print(stringIsOnly_1("WORD"))
'''
Output result：
    True
'''

def stringIsOnly_2(string):
    #如果去重之后字符串长度和原字符串长度一致，说明没有重复字符
    return len(set(string)) == len(string)

print(stringIsOnly_2("HELLO"))
print(set("HELLO"))
'''
Output result：
    False
    {'O', 'L', 'H', 'E'}
'''

'''
7.2、查找第一次出现的唯一字符
    输入一个字符串，能否找到此字符串中第一次出现的唯一字符，要求通过编程将其返回。如果字符串中不存在
唯一字符，则返回False。例如：输入：ACDDAEEF，将返回C，因为字符C和F是字符串中的唯一字符，字符C是首次
出现的。
'''

def firstOnlyStr_1(string):
    box = set()  #存放所有出现过的字符
    l = []       #根据顺序存放唯一字符
    for i in string:
        #判断不是唯一字符
        if i in box:
            if i in l:
                l.remove(i)
        else:
            box.add(i)
            l.append(i)
    #有唯一字符存在
    if len(l) > 0:
        return l[0]
    return False

print(firstOnlyStr_1("ACDDAEEF"))
'''
Output result：
    C
'''

'''
7.2、扩展
    现在要求找到第一次出现的唯一字符的位置，即：返回第一次出现的唯一字符的下标（如果没有符合
的字符，返回False）。上面代码如何进行修改。
'''

def firstOnlyStr_2(string):
    box = {}     #使用字典记录字符位置
    l = []       #根据顺序存放唯一字符
    for i in range(0, len(string)):
        c = string[i]   #取出当前下标字符
        #判断不是唯一字符
        if c in box.keys():
            if c in l:
                l.remove(c)
        else:
            box[c] = i
            l.append(c)
    #有唯一字符存在
    if len(l) > 0:
        return box[l[0]]
    return False

print(firstOnlyStr_2("ACDDAEEF"))
'''
Output result：
    1
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
16.1、统计字符串单词个数
    输入一个字符串，其为一段英文语句，要求通过编程统计其中单词个数。这里的单词指的是连续不为空格的字符串。

方法一：遍历字符串（以空格进行标记）；
方法二：分割字符串。
'''

#遍历字符串
def countWord_1(s):
    count = 0   #计数
    tmp = True  #标记是否出现空格，默认置为True
    for c in s:
        #遇到第一个非空格，进行计数
        if c != " ":
            if tmp:
                count += 1
            tmp = False
        #如果是空格，为True
        else:
            tmp = True
    return count

print(countWord_1("Hello World"))
'''
Output result：
    2
'''

def countWord_2(s):
    l = s.split()   #split()方法进行分割空格
    return len(l)

print(countWord_2("Hello World, afei"))
'''
Output result：
    3
'''

'''
16.2、末尾单词长度计算
    输入一个仅包含字母和空格的字符串。要求编写程序返回字符串中最后一个单词的长度。如果字符串中不包含单词，
返回False。例如：
'''

def endCount(s):
    l = s.split()
    if len(l) > 0:
        return len(l[-1])
    else:
        return False

print(endCount("Hello afei"))
'''
Output result：
    4
'''
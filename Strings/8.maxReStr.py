#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

''''
8、最长不含重复字符的子字符串长度
    现在输入一个字符串，要求通过编程找到其中不包含重复字符的子字符串，并将其长度返回。例如：输入AAA，将返回
结果1，输入：ABCACBBB，将返回结果3。
解题思路：
（1）以0为起点进行不含重复字符的最长子串长度计算；
（2）移动起点，再次进行不含重复字符的最长子串长度计算；
（3）重复过程2，直到起点移动到原字符串的最后一个字符位置为止。并将计算结果中的最值返回。
'''

#截取最大重复字符
#start：截取起点，s：需要截取的字符串
def maxReStr(start, s):
    box = set() #记录字符
    l = 0
    for i in range(start, len(s)):
        c = s[i]  #取出当前字符
        if c in box:
            return l
        else:
            box.add(c)
            l += 1
    return l

#入口函数：不断移动start点
def func(s):
    length = 0
    for start in range(0, len(s)):
        l = maxReStr(start, s)
        if l > length:
            length = l
    return length

print(func("ABCACBBB"))
'''
Output result：
    3
'''
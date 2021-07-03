#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
27、找到最长回文字符串
    输入一个字符串，要求编程找到其中最长的回文字符串。例如：输入"ABCBD"，需要输出"BCB"作为结果。
解题思路：
    本题可以使用决策回溯的算法解决。由于是找到最长的回文字符串，所以可以使用假设法，可以先假定一个最长的
回文字符串长度进行验证，之后再逐次缩短长度直到找到满足条件的字符串即可。这种方式比决策回溯要简单。
'''

def findMaxPalin(s):
    # 假定最大回文字符串长度与原字符串长度相同
    lenmax = len(s)
    #进行循环验证
    while lenmax > 0:
        #检查当前长度是否可以在原字符串中截取出回文字符串
        for i in range(0, len(s)):
            #当前长度不能超过原字符串长度
            if i + lenmax > len(s):
                break
            string = s[i:(i + lenmax)]
            #判断是否是回文字符串
            if string == string[::-1]:
                return string
        lenmax -= 1
    return ""

print(findMaxPalin("ABCBD"))
'''
Output result：
    BCB
'''
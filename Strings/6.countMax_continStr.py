#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
6、统计连续字符串的最大长度
    现在输入一个字符串，要求通过编程返回其中最长的连续重复字符的长度。例如：输入字符串：ABBBCDD，
将返回结果3，因为其中连续重复字符组成的子串为：BBB。
解题思路：
（1）对输入的字符串进行遍历，记录当前遍历到的字符的连续出现次数；
（2）遍历到不同的字符后，重置计数。将计算的最大值返回。
'''

def countMax_str(string):
    maxL = 0    #最大长度
    curL = 0    #当前长度
    curChar = ""  #当前字符
    #遍历字符
    for i in string:
        #首次遍历
        if curChar == "":
            curChar = i
            curL = 1
        else:
            #如果碰到相同字符，计数累加
            if i == curChar:
                curL += 1
            #如果不是相同，重置
            else:
                curL = 1
                curChar = i
        if curL > maxL:
            maxL = curL
    return maxL

print(countMax_str("ABBBCDDEE"))
'''
Output result：
    3
'''

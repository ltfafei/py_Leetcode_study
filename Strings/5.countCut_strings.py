#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
5、分割字符串获取最大分数
    现在输入一个只有0和1组成的字符串，其长度不小于2，需要将其从某个位置进行分割成左右两个子串（子串的长度
都不小于0），在左串中，每出现一个0，则记一分；在右串中，每出现一个1，则记1分。要求通过编程计算所有分割方案
中最高可以得多少分，并将分数返回。例如：输入：00111，将返回结果5，因为当左串为00右串为111时，得分最高，为
5分。
'''

def countCutStr(string):
    source = 0
    for i in range(1, len(string) - 1):
        l = string[0:i]  #左边分割
        r = string[i:]   #右边分割
        ls = l.count("0")   #左串计算0的个数
        rs = r.count("1")   #右串计算1的个数
        temp = ls + rs
        #找到组合的最大分数
        if temp > source:
            source = temp
    return source

print(countCutStr("0010111"))
'''
Output result：
    6
'''
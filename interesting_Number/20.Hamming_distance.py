#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
20、计算汉明距离
    汉明距离是二进制运算在工业上的一种应用。汉明距离常用于信息纠错、图片相似度分析、数据编码
抗干扰性分析等场景中。
汉明距离的定义：对于两个二进制数，汉明距离是指其对应位上不一致的位的个数。例如：二进制数1010
和1111，其从右向左第一位和第三位数字不同，所以他们的汉明距离为2。
    现在输入两个整数，要求通过编程计算它们之间的汉明距离。

巧用位运算解决：
    异或：置1的方法；
    与：判定1的方法；
    位移：循环判定的方法。
'''

def hamMing(m, n):
    res = m ^ n  #异或取出所有的1
    i = 0
    while res > 0:
        i += res & 1       #判定1的个数
        res = res >> 1     #右移循环判定1
    return i

print(bin(10)[2:])
print(bin(15)[2:])
print(hamMing(10, 15))

'''
Output result：
   1010
    1111
    2
'''
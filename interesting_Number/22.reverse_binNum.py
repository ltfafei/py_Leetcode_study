#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
22、颠倒二进制数
    现在给定一个32位的二进制数，将其左右颠倒后输出。即：第一位与最后一位交换，
第二位与倒数第二位交换，以此类推。通过编程实现。
'''

def reverse_binNum(N):
    tip = 0  #步长
    res = 0  #记录结果
    while tip < 32:
        tip += 1
        lastNum = N & 1  #取出二进制0和1
        res = (res << 1) + lastNum
        N = N >> 1
    return res

print(reverse_binNum(2))
print(bin(2)[2:])
print(bin(reverse_binNum(2))[2:])

'''
Output result：
    1073741824
    10
    1000000000000000000000000000000
'''
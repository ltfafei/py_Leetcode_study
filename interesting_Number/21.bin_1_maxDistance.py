#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
20、二进制数中1的最长距离
    通过前面的与运算可以很轻松的找到1的个数。现在，给定一个正整数，要求通过
编程找到这个正整数中两个连续的1之间的最长距离。例如：二进制数：1110010，其中
连续两个1之间的最大距离为3。

算法分析：
    1.首先对二进制数的每一位进行遍历，采用位移运算实现，标记
    第一个1，和第二个1的位置；
    2.当遇到1时，开始计数，并将之前的计数清零，在清零前先
    判断是否是最长距离，并存储下来；
    3.遍历结束，将所有的最长距离返回。
'''

def func(N):
    cur = -1  #标记当前位置
    max_ = 0  #标记最长距离
    while N > 0:
        if N & 1 == 1:  #找到1
            #等于1，cur置0
            if cur != -1 and max_ < cur + 1:
                max_ = cur + 1
            cur = 0
        elif cur != -1:
            cur = cur + 1
        N = N >> 1
    return max_

print(bin(9)[2:])
print(func(9))

'''
Output result：
    1001
    3
'''
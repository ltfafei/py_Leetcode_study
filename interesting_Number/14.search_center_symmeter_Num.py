#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
14、在上一篇中已经知道中心对称数是一个数字旋转180度之后看起来依旧相同的数字。
    现在，要求通过编程找到长度为N的所有中心对称数。例如：N等于2时，所有中心对称数为：
    ”11“、”69“、”88“和”96“。
中心对称数特性：
（1）中心对称数如果是奇数位的，那么最中间的数一定是：0、1、8这三个数字中的一个。因为只有
这三个数字旋转180度后依然与自身相等。并且从中心开始向两边扩展的话，两边的数字一定是成对出现的。
即：00、11、88、69和96这5对数字。
（2）如果是偶数位的，则从左向右与从右向左依次取到的数字一定是成对的。
'''

S = ['0', '1', '8']  #N=1时中心对称数
D = ["00", "11", "88", "69", "96"]  #双位两边扩展
d = ["11", "88", "69", "96"]  #N=2时中心对称数

def func(l, N):
    res = []
    #双位判断
    if N > 1:
        for i in D:
            for item in l:
                tmp = list(item)
                tmp.insert(len(tmp) // 2, i)
                res.append("".join(tmp))
        if res == []:
            res = d
        return func(res, N - 2)
    #奇数位判断
    if N == 1:
        for i in S:
            for item in l:
                tmp = list(item)
                tmp.insert(len(tmp) // 2, i)
                res.append("".join(tmp))
        if res == []:
            res = S
        return func(res, N - 1)
    return  l

print(func([], 3))

'''
Output result：
    ['101', '808', '609', '906', '111', '818', '619', '916', '181', '888', '689', '986']
'''
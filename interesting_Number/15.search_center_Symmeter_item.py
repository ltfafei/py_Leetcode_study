#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
15、现在，需要确定中心对称数的个数，即通过low和high这两个边界确定一个范围，要求通过
编程找出这个范围内的中心对称数个数。注意：不需要把所有的中心对称数都找出来，只需要
确定个数即可。
    其实，有了前面的基础，位数的就简单了，只需要将获取中心对称数列表的长度就知道个数了。
    关键还需要知道[low, high]边界范围的确定。
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

def get_cen_Symmer_item(low, high):
    mix_ = len(low)
    max_ = len(high)
    count = 0
    while mix_ <= max_:
        res = func([], mix_)
        count += len(res)
        #确定边界数
        if mix_ == len(low) or mix_ == len(high):
            for item in res:
                #剔除小于最小值和大于最大值的个数
                if int(item) < int(low) or int(item) > int(high):
                    count  -= 1
        mix_ += 1
    return count

print(func([], 1))
print(func([], 2))
print(get_cen_Symmer_item("1", "100"))

'''
Output result：
    ['0', '1', '8']
    ['11', '88', '69', '96']
    6
'''
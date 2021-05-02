#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
    强整数有这样的定义，给定两个正整数X和Y，如果某一整数等于X^I+Y^J，
其中整数I>=0且J>=0，那么我们认为该整数是一个强整数。

    现在，输入X和Y，给定一个上边界N，尝试编程找出小于等于N的所有强整数，通过列表的方式返回。
'''

import math

def strongInteher(x, y, bounds):
    l = []
    for i in range(0, bounds + 1):
        # x^i大于bounds的情况
        if math.pow(x, i) > bounds:
            break
        for j in range(0, bounds + 1):
            res = math.pow(x, i) + math.pow(y, j)
            if res <= bounds:
                if int(res) not in l:
                    l.append(int(res))
                else:
                    if x == 1:
                        return l
                    else:
                        break
    return l
print(strongInteher(2, 3, 20))

'''
Output result：
    [2, 4, 10, 3, 5, 11, 9, 17, 19]
'''

'''
程序优化：
    （1）使用元组；
    （2）使用栈结构
'''

def strongInteher2(x, y, bounds):
    l = []
    stack = [(0, 0)]
    while len(stack) > 0:
        #获取列表中的一个元素，默认是最后一个元素
        tmp = stack.pop()
        res = math.pow(x, tmp[0]) + math.pow(y, tmp[1])
        if res <= bounds:
            if int(res) not in l:
                l.append(int(res))
            # res>bounds的情况
            if x != 1:
                stack.append((tmp[0] + 1, tmp[1]))
            if y != 0:
                stack.append((tmp[0], tmp[1] + 1))
    return l
print(strongInteher2(2, 3, 22))

'''
Output result：
    [2, 4, 10, 11, 13, 17, 5, 7, 19, 3, 9]
'''
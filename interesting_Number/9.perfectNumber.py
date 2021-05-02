#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
9、对于一个正整数，如果它和除了它以外的所有正因子之和相等，则称这个数为完美数。
    现在，给定一个数N，判断它是否是完美数。如：28 = 1+2+4+7+14

解题思路：
    首先需要将这个数N的所有的因数找出来，拿到所有的因数相加，如果等于N，
    则说明是完美数，否则不是。这里有一个技巧：找到了一个因数，另一个也就找到了，
    除了1和它本身，是成对出现的。
    
    完美数，又称为完全数或完备数。自然中的第一个完美数是6，数字6也往往有着特殊的寓意。
据史料记载，最早开始研究完美数的人是公元前6世界的毕达哥拉斯。当时他已经找到了世上存在的两个完美数：
6和28，毕达哥拉斯曾说: 6象征着完美的婚姻以及健康和美丽，因为它是完整的，其所有因数的和等于它自身。除此之外，
一些《圣经》信仰者也认为6和28是上帝创造世界时所使用的基本数字，上帝创造世界花了6天，28天则是月亮绕地球一周的日数。
在我国古代文化中，数字6和28也被赋予了更多了含义，例如：与6有关的六畜、六谷、六常等，与28相关的二十八星宿等。
完美数仿佛有着神奇的魔力，在历史中总是有许多巧合与之相关。
    目前为止，到底存在多少个完美数依然是个谜，寻找完美数的过程并不十分轻松。到2013年2月6日，人们一共发现了48个完美数。
同样，完美数是十分稀有的，第13位完美数的长度就已经达到314位，之后完美数的长度则更加恐怖，据估计，
将第39位完美数使用4号字打印出来的长度有一本字典那么厚。自从人们发现完美数后，
众多数学家和数学爱好者都不知疲倦的寻找自然界中存在的完美数，这是一个艰苦的过程，直到计算机科学的发展，
对完美数的寻找效率才得到了质的提高。非常神奇的是，至今为止，所有找到的完美数都是偶数，尚无有奇完美数被发现。
'''

import math

def perfectNumber(N):
    if N <= 0:
        return False
    res = 0
    
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            res += i
            #剔除两个因子相同的情况
            if i * i != N:
                res += N / i
    #因为是成对出现，所以需要乘以2
    if res == N * 2:
        return True
    return False
print(perfectNumber(28))

'''
Output result：
    True
'''

'''
    查表法：在33550336以内的完美数只有五个：6、28、496、8128和33550336
'''

def checkPerfectNumber(N):
    return True if N in [6, 28, 496, 8128, 33550336] else False
print(checkPerfectNumber(8128))

'''
Output result：
    True
'''
#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
7、酒瓶子问题
    假设一个酒馆中现在有这样一个优惠活动：没N个空瓶子可以换一瓶新酒，如果一个人他买了M瓶酒，则参加
这个优惠活动他最终可以喝多少瓶酒。要求使用编程解决该问题。现在输入购买的酒树m和兑换活动中兑换一瓶新酒所需的空酒瓶n，返回最终可以喝到几瓶酒。例如：输入：m=5, n=5, 则最终可以喝到6瓶酒。
'''

def beerBottle(m, n):
    #空酒瓶取整+新酒树
    res = (m // n) + m
    return res

print(beerBottle(3, 3))
'''
Output result：
    4
'''
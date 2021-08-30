#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
1、上楼梯问题
    现在有一个n阶台阶，小明同学可以每次选择上1节台阶，也可以选择上2阶台阶。如果需要最终刚好登有台阶。
那小明有多少种方式可选，要求使用编程解决。例如：假设楼梯台阶有3阶，那么小明有3种选择：
（1）每次上一阶台阶；（2）先上一阶再上两阶；（3）先上两阶再上一阶。
解题思路：抽象问题，递归回溯解题。
'''

from functools import lru_cache

#入口函数
def walkDownstairs(n):
    return ways(n)
#该装饰器为递归函数增加缓存策略，提供性能
@lru_cache()
def ways(n):
    #只剩一阶台阶，只有一种上楼方式
    if n<= 1:
        return 1
    # 只剩2阶台阶，只有2种上楼方式
    if n == 2:
        return 2
    #2种方式进行递归计算
    ways1 = ways(n-1)
    ways2 = ways(n-2)
    return ways1 + ways2

print(walkDownstairs(9))
'''
Output result：
    55
'''

'''
    如果输入的n非常大，可能会导致整数溢出的情况，如果只需要验证结果是否正确，可以对
1000000007进行取模运算，既上面的：return (ways1 + ways2) % 1000000007
'''
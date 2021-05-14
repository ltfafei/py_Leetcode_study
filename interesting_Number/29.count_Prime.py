#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
29、计算质数
    给定一个非负整数，尝试统计所有小于N的质数的个数。
解题思路：全遍历
'''

import math

#判断质数
def isPrime(n):
    i = 2   #从2开始，1本身不是质数
    while i <= int(math.sqrt(n)):    #如果小于n的开方，说明不是质数
        if n % i == 0:
            return False
        i += 1
    if n >= 2:
        return True
    return False

def count_Prime1(n):
    c = 0   #质数计数
    for i in range(0, n):
        if i < 2:
            continue
        if isPrime(i):
            c += 1
    return c

print(count_Prime1(92000))
'''
Output result：
    8887
'''

'''
程序优化：
    当输入一个很大的数时，使用上面这种方法判断太费时间。因为首先要判断是否是质数，
再取出质数的个数。但是，通过厄拉多筛选法可以直接判断出一个数有多少个质数。
厄拉多筛选法：
    厄拉多是一位古希腊数学家，关于寻找质数，他发明了一种与众不同的方法。即：厄拉多筛选法。
假设需要寻找100以内的质数，按照厄拉多筛选法，首先可将100格子的容器(列表)分别表示0-99这100
个数字。如果某个格子表示的数字为质数，则在这个格子中放入圆球标记，如果不是质数，则让它空着，
开始时，把除了0和1之外的盒子放入圆球，从第三个盒子开始判断，如果2是质数，则将所有表示2的倍数
的盒子拿走以此类推，最后所有非空的盒子所表示的数字就是被筛选出来的质数，只需要计算它们的个数
即可。
'''

def count_Prime2(n):
    if n < 2:   #如果n小于2，说明不存在质数
        return 0
    l = [1] * n
    l[0] = 0
    l[1] = 0
    c = 1   #第三位2是质数
    i = 3   #从第四位开始判断
    while i < len(l):
        if l[i] != 0:   #判断是质数
            c += 1
            j = 3
            #将偶数位剔除
            while i * j < len(l):
                l[i * j] = 0
                j += 2
        i += 2
    return  c

print(count_Prime2(92000))
'''
Output result：
    8887
'''
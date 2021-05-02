#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
18、输入两个二进制表示的字符串类型的数值，要求通过编程计算它们相加的和。注意：
输入的二进制字符串不为空，并且只包含0和1两种字符。
手动求和方法：
    了解进制在数学运算中的本质原理，解决本题就简单。首先，加法运算可以从右向左进行，
处于相同位的数字进行相加，如果两个运算数的位数不同，则较小的数的空白位用0补齐。
对于二进制，其本质是逢二进一。所以在运算时可以采用一个变量记录是否进位，根据二进制
的法则从右向左计算即可。
'''

def bin_sum_1(M, N):
    i = 0
    res = ""  #存放结果
    tip = 0   #进位
    while i < len(N) or i < len(M) or tip == 1:
        tmp1 = 0
        tmp2 = 0
        if i < len(M):
            tmp1 = int(M[len(M)-1 - i]) #去下标进行相加
        if i < len(N):
            tmp2 = int(N[len(N)-1 - i])
        tmp = tmp1 + tmp2 + tip
        if tmp >= 2:  #如果相加大于等于2情况
            tmp -= 2
            tip = 1
        else:
            tip = 0
        res = str(tmp) + res
        i += 1
    return res

print(bin_sum_1("01011", "10011"))

'''
Output result：
    11110
'''

'''
python内置函数方法进行二进制求和
'''
def bin_sum_2(M, N):
    res = bin(int(N, 2) + int(M, 2))[2:]
    return res

print(bin_sum_2("01101", "10110"))
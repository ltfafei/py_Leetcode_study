#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
25、阶乘尾数
    阶乘在数学中使用!表示，即：5!表示5的阶乘，展开就是：1 * 2 * 3 * 4 * 5 = 120。如果输入一个非常大的数，
它的阶乘结果也会很大，那么计算就会耗费时间。现在通过编程计算出阶乘结果中末尾有几个0，例如：输入5的时候
结果为1。

阶乘尾数末尾0特点：
    只有0-9中的偶数(2、4、6、8)和5相乘才会出现末尾为0的情况。
所以，要得到阶乘末尾有几个0，只需要计算原数可以拆解为多少个因子5即可。
'''

def factorial_Mantissa(num):
    res = 0
    while num/5 > 0:
        res += int(num/5)
        num = int(num/5)
    return res

print(factorial_Mantissa(5))
'''
Output result：
    1
'''
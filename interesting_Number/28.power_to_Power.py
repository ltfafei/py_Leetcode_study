#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
28、幂次方
    在数学中，求N个相同的数的乘积的运算被称为乘方运算，其运算结果被称为幂。
现在，要求通过编程实现输入一个数m，判断它是否是n的幂次方。
'''

def power_Check(m, n):
    s = n
    while s < m:
        s *= n  #进行n的累乘
    if m == 1 or s == m:
        return True
    return False

print(power_Check(4, 2))

'''
Output result：
    True
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
19、十进制数的反码
    补码和反码是数字存储的一种机制。每个十进制数都可以使用二进制表示，所谓反码就是将
十进制数用二进制表示，并且将每一个二进制位进行取反操作。例如：数字5的二进制为：101，
其反码为：010。
    现在，要求通过编程实现输入一个十进制数，返回其反码对应的十进制数。
'''

def dec_rever_code(num):
    c = 1
    while c < num:
        c = (c << 1) + 1  #每次左移1位补1
    return c ^ num   #异或取反码

print(dec_rever_code(11))
#十进制对应的二进制数
print(bin(11)[2:])
#反码对应的二进制数
print(bin(dec_rever_code(11))[2:])

'''
Output result：
    4
    1011
    100
'''
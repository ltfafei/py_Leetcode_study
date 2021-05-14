#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
31、整数转换
    现在输入两个整数A和B，尝试编写一个函数，计算最少需要改变多少位，才能将数字A转换成数字B。
注意：
    由于bin()函数的缺陷：bin()函数中正数没有问题，但是负数会转换成正数，这与负数在二进制中
转换有出入，负数表示二进制是通过补码的形式转换的。
'''

def integerTrans(A, B):
    #与32位1进行与运算获取补码
    A = A & 0xffffffff
    B = B & 0xffffffff
    res = A ^ B  #异或得到1
    c = bin(res).count("1")  #获取1的个数
    return c

print(integerTrans(-1, 1))
print(bin(-1 & 0xffffffff)[2:])
print(bin(1)[2:])

'''
Output result：
    31
    11111111111111111111111111111111
    1
'''
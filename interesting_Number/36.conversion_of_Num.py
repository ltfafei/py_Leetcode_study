#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
(10101)2 = 1*2^4 + 0*2^3 + 1*2^2 + 0*2^1 + 1^2^0

    现在，输入一个M进制的数N转换为十进制如何用表达式表示？，要求编程实现。
'''

#（1）解决输入一个M进制的数N转换为十进制如何用表达式表示
#input接收变量赋值默认为str类型,函数接收变量赋值默认为int类型
def conversionNum1(M,N):
    L = len(str(N))
    #第一种变量格式化方法
    res = "%s*%s^%d" %(str(N)[0], M, L-1)
    for i in range(1, L):
        if str(N)[i] != "0":
            res = res + '+' "%s*%s^%d" %(str(N)[0], M, L-i-1)
    return res
print(conversionNum1(2, 10101))

'''
Output result：
    1*2^4+1*2^2+1*2^0
'''

def conversionNum2(M,N):
    L = len(str(N))
    #第二种变量格式化方法
    res = "{}*{}^{}".format(str(N)[0], M, L-1)
    for i in range(1, L):
        if str(N)[i] != "0":
            res = res + '+' "{}*{}^{}".format(str(N)[0], M, L-i-1)
    return res
print(conversionNum2(8, 666))

'''
Output result：
    6*8^2+6*8^1+6*8^0
'''

def conversionNum3(M,N):
    L = len(str(N))
    #第三种变量格式化方法，python3.6引入f-string方法
    res = f'{str(N)[0]}*{M}^{L-1}'
    for i in range(1, L):
        if str(N)[i] != "0":
            res = res + '+' f'{str(N)[0]}*{M}^{L-i-1}'
    return res
print(conversionNum3(3, 12345))

'''
Output result：
    1*3^4+1*3^3+1*3^2+1*3^1+1*3^0
'''

#使用列表实现
def conversionNum4(M,N):
    L = len(str(N))
    res = []
    for i in range(1, L):
        if str(N)[i] != "0":
            res.append(f'{str(N)[0]}*{M}^{L-i-1}')
            sum = '+'.join(res)
    return sum
print(conversionNum4(3, 123))

'''
Output result：
    1*3^1+1*3^0
'''
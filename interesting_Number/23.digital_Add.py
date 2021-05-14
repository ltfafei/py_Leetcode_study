#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
23、各位相加
    现在输入一个非负整数，将这个数字的每一位上的数字提取出来并进行累加，将最后的
累加结果返回。通过编程实现。例如：输入数字21，累加就是2+1=3
'''

def digital_Add(num):
    L = list(str(num))  #转换为列表提取出每一位
    res = 0
    for i in L:
        res += int(i)
    return res

print(digital_Add(123123))
'''
Output result：
    12
'''

'''
扩展：
    现在需要累加每次都为个位数。意思是累加之后大于9，继续累加直至累加结果位个位数
'''

def digital(num):
    res = num
    #如果大于9，继续累加
    while res > 9:
        tmp = res
        res = 0
        t = list(str(tmp))
        for i in t:
            res += int(i)
    return res

print(digital(123123))
'''
Output result：
    3
'''

'''
挑战：
    不使用循环和递归实现各位相加。
解题：
    从数的特征入手。如：abc = 100*a + 10*b + c = 99a + 9b + (a+b+c)
'''

def digital2(num):
    if num == 0:
        return 0
    res = num % 9   #对9取余如果为0，直接返回9
    if res == 0:
        return 9
    else:
        return res

print(digital2(123123))
'''
Output result：
    3
'''
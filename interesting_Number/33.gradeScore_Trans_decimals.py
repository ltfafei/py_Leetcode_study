#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
33、分数转小数
    在数学中，分数和小数是可以相互转换的，现在给定两个整数A和B，分别表示分子和分母，要求
通过编写程序，将其转换成小数，需要输出字符串类型的数据，并且如果循环小数，需要将其循环的
部分包在括号内。例如：A=1，B=3，则输出：0.(3)。
难点：
（1）如何处理计算结果的正负问题；
（2）如果是循环小数，如何判断出现循环的方法；
（3）如果是循环小数，如何确定循环的位置，并插入小括号。

算法思路：
（1）首先用分子整除分母，得到小数点前的数字；
（2）如果分子除以分母有余数，将余数取出，让余数乘以10作为新的分子；
（3）用新的分子整除分母，得到的数字依次往小数点后追加；
（4）重复2和3步骤，直到没有余数，或者出现重复的余数时，就添加小括号。
'''

def grade_Trans_decimals(A, B):
    #如果分子为0，那么结果就为0
    if A == 0:
        return "0"
    res = ""
    #如果为负数情况，则添加一个负号
    if (A < 0 and B > 0) or (A > 0 and B < 0):
        res += "-"
    res = res + str(int(A / B))  #能除尽的情况
    #如果有余数，则添加小数点
    if A % B != 0:
        res += "."
    dic = dict()    #存放余数，便于找到循环的位置
    while A % B != 0:
        tmp = A % B
        tmp *= 10
        if tmp in dic.keys():
            #确定循环小数位置，并插入()
            l = list(res)
            l.insert(dic[tmp], "(")
            l.append(")")
            res = "".join(l)
            break
        dic[tmp] = len(res)
        res += str(int(tmp / B))
        A = tmp
    return res

print(grade_Trans_decimals(1, 3))
'''
Output result：
    0.(3)
'''
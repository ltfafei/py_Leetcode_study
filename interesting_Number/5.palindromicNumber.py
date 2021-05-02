#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
5、"回文"是指一个句子正读和反读都能读通，在数学中也有这样一类数字有这样的特征，
被称为“回文数”。回文数是指正序（从左到右）和倒序（从右到左）读都是一样的整数。

    现要求输入一个整数N，判断其是否是回文数。
    
解题思路：
    将输入的数转为列表，通过列表的逆序判断是否是回文数。
'''

def palindromicNumber(N):
    list1 = list(str(N))
    list2 = list(str(N))
    list2.reverse()
    return list1 == list2

print(palindromicNumber(121))

'''
Output result：
    True
'''

'''
程序优化：
    使用切片减少代码量
'''

def palindromicNumber2(N):
    # -1代表从右往左，第二位代表步长
    return str(N) == str(N)[::-1]
    
print(palindromicNumber2(112111))

'''
Output result：
    False
'''
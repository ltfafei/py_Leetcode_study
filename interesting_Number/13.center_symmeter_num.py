#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
13、中心对称数定义：一个数字旋转180度之后看起来依旧相同的数字。例如：数字69旋转
180度之后依然为69，则数字69是一个中心对称数。
    现在，输入一个任意的字符串形式的数字，要求通过编程判断它是否是中心对称数。
'''

def func(num):
    #数字0-9建立映射关系
    dic = {"0":"0", "1":"1", "2":"-1", "3":"-1", "4":"-1", "5":"-1", "6":"9", "7":"-1", "8":"8", "9":"6"}
    l = []
    for i in num:
        if dic[i] == "-1":
            return False
        #每次插入到第一个元素位置，自动逆序
        l.insert(0, dic[i])
    return  num == "".join(l)

print(func("96"))

'''
Output result：
    True
'''
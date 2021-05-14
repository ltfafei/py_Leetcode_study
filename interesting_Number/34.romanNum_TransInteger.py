#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
34、罗马数字转整数
罗马数字表示：
    I   #表示数值：1
    V   #表示数值：5
    X   #表示数值：10
    L   #表示数值：50
    C   #表示数值：100
    D   #表示数值：500
    M   #表示数值：1000
罗马数字书写规则：
    一般情况下罗马数字在编写时，如果小的数字出现在大的数字的右边，则它们是相加关系。例如数值2
会写作II；当小的数字出现在大的数字左边时，它们是相减关系。例如：数值4会写作IV。对于小的数字出现
在大的数字左边的情况，只有如下几种：
    IV  #4
    IX  #9
    XL  #40
    XC  #90
    CD  #400
    CM  #900

    现在输入一个字符串类型的罗马数字，将其转换为整数输出，数值的输入范围大于0且小于4000。
'''

def romanNum_TransInteger(num):
    #罗马数字与数值建立映射关系
    dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    res = 0
    for i in range(0, len(num)):
        if i < len(num) - 1:
            j = i + 1
            n1 = num[i]  #取出第一个罗马数字
            n2 = num[j]  #取出第二个罗马数字
            #进行左右大小判断
            if n1 >= n2:
                res += dic[num[i]]
            else:
                res -= dic[num[i]]
        else:
            res += dic[num[i]]
    return res

print(romanNum_TransInteger("IV"))
'''
Output result：
    4
'''
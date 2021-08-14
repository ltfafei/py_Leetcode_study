#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
4、根据条件获取列表中的值
   现在输入一个列表，列表中存放的全部是整数。要求通过编程返回列表中第三大的整数，注意：如果存在重复元素，则需要
过滤，如果列表中元素不足三个，则返回该列表中最大的整数即可。例如：输入[1,2,2,5]，则需要返回1作为答案；如果输入
[5,10]，则需要返回10作为答案。
'''

def confitionGetValue(l):
    l = list(set(l))
    m1 = max(l)
    l.remove(m1)  #移除第一大整数
    m2 = max(l)
    l.remove(m2)  #移除第二大整数
    m3 = max(l)
    return m3    #返回第三大整数

print(confitionGetValue([1,2,2,5]))
'''
Output result：
    1
'''
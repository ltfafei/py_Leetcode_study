#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
6、寻找重复次数最多的元素
    现在输入一个拥有N个元素的列表，列表中存在某个元素，其出现的次数大于（N/2）。要求通过编程将这个元素找到。例如：
输入[3,2,3,3,2,3,1]，需要返回3作为答案。
'''

def findRepemaxStr(l):
    dic = {}  #以元素和出现次数为键值对存储
    for i in l:
        #该元素已在字典中出现，进行累加
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = i
        if dic[i] > len(l)/2:
            return i

print(findRepemaxStr([3,2,3,3,2,3,1]))
'''
Output result：
    3
'''
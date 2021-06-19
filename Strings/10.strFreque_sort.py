#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
10、根据字符串出现频率进行排序
    现在输入一个字符串，能否编程重新对字符串得字符进行排序，按照其中字符的出现频率降序进行排序。例如：输入
字符串HELLO，需要返回LLEHO、或LLEOH、或LLHEO等。因为元字符串中只有LL出现了2次，其余字符都只出现了1次，只
需要将L字符排序到字符串的前面即可。
解题思路：
    根据字符串出现的频率进行重排序，可以通过遍历字符串，将字符串中所有出现过的字符的出现次数进行统计，可以
使用dict字典数据结构。可以用dict[key]存储字符，dict[value]存储字符出现的次数。然后根据出现次数对字典进行
降序排序即可。
'''

def strFreque_sort_1(s):
    dic = {}
    #遍历字符串
    for c in s:
        #判断字符是否出现过，如果出现过，次数+1
        if c in dic.keys():
            dic[c] += 1
        #如果没有出现过，将该字符次数赋值为1
        else:
            dic[c] = 1
    #dic.items()返回一组元组，lambda表达式排序lambda x: x[1]根据元组的第二个元素排序
    l = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    res = ""
    #遍历列表统计字符次数
    for item in l:
        count  = item[1]    #字符次数
        char = item[0]      #字符
        while count > 0:
            res += char
            count -= 1
    return res

print(strFreque_sort_1("HELLO"))
'''
Output result：
    LLHEO
'''

#遍历列表统计字符次数优化
def strFreque_sort_2(s):
    dic = {}
    for c in s:
        if c in dic.keys():
            dic[c] += 1
        else:
            dic[c] = 1
    #dic.items()返回一组元组，lambda表达式排序lambda x: x[1]根据元组的第二个元素排序
    l = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    res = ""
    #遍历列表统计字符次数
    for item in l:
        res += item[0] * item[1]
    return res

print(strFreque_sort_2("HELLO"))
'''
Output result：
    LLHEO
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
24、比较语句差异
    输入两个字符串，分别表示两个语句，要求编程找出语句中的差异单词有哪些？所谓的差异单词，是指没有同时出现
在两个语句中的单词（语句中单词以空格进行分割，不存在标点符号）。例如：输入两个单词为："hello afei", "hi afei"
，则返回["hello", "hi"]
解题思路：利用集合去重的特性找到两个字符串的差集。
'''

def compareStatdiff(w1, w2):
    w1 = w1.split()
    w2 = w2.split()
    set1 = set(w1)
    set2 = set(w2)
    set3 = set1.difference(set2)
    set4 = set2.difference(set1)
    return list(set3) + list(set4)

print(compareStatdiff("hello afei", "hi afei"))
'''
Output result：
    ['hello', 'hi']
'''
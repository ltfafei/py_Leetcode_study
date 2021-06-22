#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
19、计算单词的最短距离
    输入一个列表，列表中存放的全部是单词，再输入两个单词，要求通过编程找到两个单词再列表中的最短距离。注意：
列表中的单词可能出现重复。例如：输入["hello", "world", "hi", "afei", "hello"]，输入的两个单词："hello", "afei",
则它们再列表中的最短距离为1。
解题思路：
（1）遍历列表，找到指定单词在其中的位置并使用列表进行记录，同一个单词可能出现多次；
（2）对记录的列表进行遍历，找到距离单词最近的两个位置。
'''

def countWord_minDistance(wordLinst, w1, w2):
    l1 = []  #存放w1
    l2 = []  #存放w2
    for i in range(0, len(wordLinst)):
        w = wordLinst[i]
        #记录两个单词的位置
        if w == w1:
            l1.append(i)
        if w == w2:
            l2.append(i)
    res = -1
    #遍历寻找最小距离
    for i in l1:
        for j in l2:
            if i == j:
                continue
            if res == -1:
                res = abs(i - j)
            else:
                r = abs(i - j)
                if r < res:
                    res = r
    return res

print(countWord_minDistance(["hello", "world", "hi", "afei", "hello"], "hello", "afei"))
'''
Output result：
    1
'''
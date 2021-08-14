#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
32、查找高频单词（堆）
    输入一组单词，请使用堆排序的方式将列表按照单词出现的频率从大到小进行排序并放入新的列表中，并且每个
元素只出现一次，例如输入列表为：
["A", "E" , "A", "F", "A", "A", "F", "E", "I", "F"]，则需要返回结果为：
["A", "F", "E", "I"]
堆：堆是一种完全二叉树，堆中每个节点都不大于/不小于其父节点的值。
大根堆：父节点大于每个节点；
小根堆：父节点小于每个节点。
解题思路：
（1）定义一个自定义单词结构用来存储单词与其出现的频次；
（2）对定义的自定义结构实现小于运算符的比较方法，方便对其进行堆构建；
（3）对输入的单词列表进行遍历，统计每个单词出现的频次；将统计完成的单词结构依次加入堆中，再从堆中依次
将单词元素取出，放入列表即完成排序。
'''

#定义单词存储结构
class Word:
    def __init__(self, word, count):
        self.word = word  #当前单词
        self.count = count  #单词出现次数
    #重载小运算符方法
    def __lt__(self, other):
        return self.count < other.count

import heapq  #该模块构建堆
def findHigh_frequency(words):
    dic = dict()  #统计词频
    #遍历获取单词出现次数
    for w in words:
        if w in dic.keys():
            dic[w].count += 1
        else:
            dic[w] = Word(w, 1)
    #
    res = []  #结果列表
    heap = []  #堆结构
    #将字典元素压入堆中，依赖小运算符方法构建堆
    for item in dic.values():
        heapq.heappush(heap, item)  #构建的为小跟堆
    for i in range(len(heap)):
        res.insert(0, heapq.heappop(heap).word)   #逆序
    return res

print(findHigh_frequency(["A", "E" , "A", "F", "A", "A", "F", "E", "I", "F"]))
'''
Output result：
    ['A', 'F', 'E', 'I']
'''
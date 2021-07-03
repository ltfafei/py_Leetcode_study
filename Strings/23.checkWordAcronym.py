#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
23.1、判断单词是否有相同的缩写
    现在规定，单词的缩写规则是取单词的首尾字母和将中间省略的字母个数统计后的数字组合作为后作为新的缩写后的结果。
例如：单词“HELLO”缩写后为：H3O。现在输入一个单词列表，要求通过编程判断其中是否存在缩写结果一样的单词，如果有
返回True，如果没有返回会False。例如：输入：["DOOR", "DEER", "AFEI"]，结果将返回True。
'''

#单词缩写
def WordAcronym(word):
    if len(word) < 3:
        return word
    #返回每个单词缩写结果
    return word[0] + str(len(word) - 2) + word[-1]

def isAcronym(l):
    tmp = []
    for i in l:
        s = WordAcronym(i)
        if s in tmp:
            return True
        tmp.append(s)   #将转换后的结果放入tmp[]临时列表
    return False

print(isAcronym(["DOOR", "DEER", "AFEI"]))
'''
Output result：
    True
'''

'''
23.2、列举单词缩写的所有形式
    单词的缩写可以有很多种模式。例如对于word的缩写，可以缩写成如下形式（不会出现数字相邻的情况）：
"word, 1ord, w1rd, wo1d, wor1, 2rd w2d, wo2, 1o1d, 1or1, w1r1, 1o2, 2r1, 3d, 4"。现在，输入
一个单词，要求通过编程将其所有缩写情况以列表形式返回。
解题思路：
（1）定义一个递归函数，传入一个start作为起点，传入一个word作为要处理的单词，判断如果起点不小于单词的长度，
则表明已经处理完成，将单词直接添加到结果列表；
（2）从起点开始遍历单词，每遍历到一个字符都有两种选择，其一是将从起点到这个字符的所有字符进行缩写，其二
是不进行缩写；
（3）在第三步的基础上，如果要进行缩写，则将其缩写后的结果进行存储，并将字符串的后半部分继续递归处理。如果
不进行缩写，直接递归处理。
（4）在上面的核心逻辑下，需要处理两个细节。一是数字不能连续，如果上一个字符是数字，则当前字符不能进行缩写
，二是最终结果中可能存在重复，需要去重之后返回。
'''

def listWordAcronym(word):
    res = []
    #枚举数字，方便枚举
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    def sele(start, w):
        #起点不小于单词长度情况
        if start >= len(w):
            res.append(w)
        for index in range(start+1, len(w)+1):
            if w[start - 1] not in nums:
                sele(index, w)
                #可以缩写处理
                temp = w[:start] + str(index - start) + w[index:]
                sele(start+1, temp)  #缩写为完成直接判断处理
            else:
                sele(index, w)
        return res
    return list(set(sele(0, word)))  #set()去重

print(listWordAcronym("word"))
'''
Output result：
    ['word', 'wor1', 'w3', '2r1', 'wo2', 'wo1d', '1ord',
     '2rd', 'w1rd', '1o1d', 'w1r1', '1o2', '3d', '1or1', 'w2d', '4']
'''
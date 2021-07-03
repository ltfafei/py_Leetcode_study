#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
25、分析词组
    输入两个单词A和B，其中单词B如果出现在A之后，则会组成AB词组，输入一个字符串语句，要求通过编程找到句子中
AB词组后跟的第一个单词（忽略大小写），答案可能存在多个，需要返回一个列表。例如：输入的A、B单词为："I", "like"
，输入语句为："I like coffee, I like afei"，则输出结果：["coffee", "afei"]
'''

def analyPhrase(A, B, s):
    tmp = 0  #临时变量计数标记
    l = s.split()
    res = []
    for w in l:
        #当计数为2时，表明前面已组成词组
        if tmp == 2:
            res.append(w)
        #词组的第一个单词
        if w == A:
            tmp = 1
        #词组的第二个单词，且前面是第一个单词
        elif w == B and tmp == 1:
            tmp = 2
        else:
            tmp = 0  #重置计数
    return res

print(analyPhrase("I", "like", "I like coffee, I like afei"))
'''
Output result：
    ['coffee,', 'afei']
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
20、字母组成单词
    输入一个列表，其中存放一组单词。同时输入一个字符串，其表示一组字符。要求使用字符串中的字符拼成列表中
的单词（字符串中的每个字符只能使用一次），程序输出所有能够组成的单词。例如：输入一组单词为["hello",
"afei"]，输入的字符串为："abdhife"，字符串中能够组成列表中的单词只有afei，因此需要返回["afei"]作为结果。
'''

def letterGroupWord(wordList, s):
    res = []
    for w in wordList:
        can = True  #标记可以组成单词
        tmp = list(s)
        #从字符串中循环遍历取出字符
        for c in w:
            #每使用一次将字符移除
            if c in tmp:
                tmp.remove(c)
            else:
                can = False
                break
        if can:
            res.append(w)
    return res

print(letterGroupWord(["hello", "afei"], "abdhife"))
'''
Output result：
    ['afei']
'''
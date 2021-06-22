#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
17、常用单词计算
    输入一个字符串，其为一个完整段落，再输入一个列表，列表中存放的是禁用词汇。要求通过编程统计出段落中出现次数最多
的单词，但是此单词不能在禁用词汇列表中。注意：段落中出现的大写字母，需要在统计过程中忽略大小写。禁用列表中所有字母
使用小写。并且段落中可能出现两个次数一样多的单词，这两个单词都可以作为常用单词，只需要返回其中一个即可。并且段落
中可能出现的标点符号有：！(感叹号)、?(问号)、‘(单引号)、,(逗号)、;(分号)和.(句号)这六种。
例如输入段落和禁用单词："I love programme, My name is afei. Hello world, i am come. hi, afei, i am robot. I am you, my name
is afei." , ["i"]，以上将返回：afei，因为在该段落中afei出现了3次，出现次数最多。

解题思路：
（1）将所有标点符号进行剔除，防止由于标点造成单词的认定混淆；
（2）将段落以单词为维度进行分割，并统计每个单词出现的次数，统计时需忽略大小写（全部转换为小写即可）；
（3）过滤禁用列表中的单词。
'''

#par：段落，dicList：禁用单词列表
def commonWordCount(par, dicList):
    newStr = ""
    for c in par:
        #过滤标点符号
        if c == "!" or c == "?" or c == "'" or c == "," or c == ";" or c == ".":
            newStr += " "
        else:
            newStr += c
    l = newStr.split()  #分割空格
    dic = {}
    for item in l:
        item = item.lower()
        #统计次数
        if item in dic.keys():
            dic[item] += 1
        else:
            #该单词第一次出现，计数为1
            dic[item] = 1
    #sorted()结合lambda表达式让单词从大大小排序
    res = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for i in res:
        #判断单词是否在禁用列表中
        if i[0] in dicList:
            continue
        return i[0]
    return False

print(commonWordCount("I love programme, My name is afei. Hello world, i am come. "
                      "hi, afei, i am robot. I am you, my name is afei.", ["i"]))
'''
Output result：
    afei
'''
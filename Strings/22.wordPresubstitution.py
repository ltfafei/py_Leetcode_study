#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
22、单词前缀替换
    输入一个列表，列表中存放的是一组单词前缀，再输入一个字符串，字符串描述的是一个英文语句。如果字符串中有
单词的前缀包含在列表中，则此单词替换成对应的前缀。例如：输入单词前缀["HE", "PY", "AF"]，输入字符串列表为
"HELLO PYTHON ME AFEI"
解题思路：
（1）对前缀列表根据前缀的长度升序进行排序；
（2）将语句分割成单词组，对单词组中的每个单词前缀进行验证，如果满足要求，则进行替换。
'''

def wordPresub(preList, strList):
    pre = []
    #根据单词前缀升序进行排序
    for i in preList:
        insert = False  #定义插入状态
        for index in range(0, len(pre)):
            w = pre[index]  #取出任一单词
            #如果当前单词更短，将其插入
            if len(i) < len(w):
                pre.insert(index, i)
                insert = True
                break
        if not insert:
            pre.append(i)
    l = strList.split()
    res = []
    #分割词组对单词前缀进行验证
    for i in l:
        insert = False
        for j in  pre:
            if i.startswith(j):  #获取前缀
                res.append(j)
                insert = True
                break
        if not insert:
            res.append(i)
    return " ".join(res)

print(wordPresub(["HE", "PY", "AF"], "HELLO PYTHON ME AFEI"))
'''
Output result：
    HE PY ME AF
'''
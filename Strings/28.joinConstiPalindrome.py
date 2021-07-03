#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
28、拼接构成回文字符串
    现在输入一组不重复的字符串，要求编程找出所有成对拼接后可以组成回文串的子串组合，以索引列表格式返回。
例如：输入["ABBC","CBBA", "SLL", "LS"]，则返回[[0,1], [1,0], [2,3]]作为结果，因为"ABBCCBBA", "CBBAABBC",
"SLLLS"都可以组成回文字符串。
解题方法：直接遍历列表字符串
'''

def joinConstiPalin(l):
    res = []
    #遍历列表元素个数
    for i in range(len(l)-1):
        #遍历每个元素(字符串)
        for j in range(i+1, len(l)):
            #去除i和j取到同一个字符的情况
            if i == j:
                continue
            s = l[i] + l[j]
            s2 = l[j] + l [i]
            #逆序判断回文串
            if s == s[::-1]:
                res.append([i, j])
            if s2 == s2[::-1]:
                res.append([j, i])
    return res

print(joinConstiPalin(["ABBC","CBBA", "SLL", "LS"]))
'''
Output result：
    [[0, 1], [1, 0], [2, 3]]
'''
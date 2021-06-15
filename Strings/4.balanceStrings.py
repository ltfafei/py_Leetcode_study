#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
4.1、平衡字符串
    现在输入一个只包含L和R的字符串，并其中L与R的个数是相等的。符合这种输入条件的字符串称之为”平衡字符串“。
要求通过编程对输入的平衡字符串进行分割，尽可能多的分割出平衡字符串子串，并将可以得到的子串数量返回。
例如：输入：RLLRRRL，将返回结果：3，其可以分割成：RL、LLRR和RL；输入：LLLRRR将返回结果：1，因为其只能分割
出LLLRRR。
'''

def balanceStrings(string):
    res = 0  #最终组合结果
    lc = 0   #L字符的个数
    rc = 0   #R字符的个数
    #对字符串进行遍历
    for i in string:
        if i == "L":
            lc += 1
        if i == "R":
            rc += 1
        #字符R和L个数相同
        if rc == lc:
            res += 1
            #重置
            lc = 0
            rc = 0
    return res

print(balanceStrings("RLLLRRRL"))
'''
Output result：
    3
'''

'''
4.2、分割回文字符串
    要求输入一个字符串，将此字符串分割成一些子串，使得每个子串都是回文字符串（单字符的字符串也属于
回文字符串）。要求通过编程将所有的分割结果返回。例如：输入字符串“abb”，返回
[
["a", "b", "b"], ["a", "bb"]
]这个二维列表作为答案（列表中元素位置可以变动）。
'''

def isPlalind(string):
    #逆序判断是否是回文字符串
    return string == string[::-1]

#start：起始位置，string：分割字符串
#l：已经产生回文串子列表，res：存放结果
def cut_plalindString(start, string, l, res):
    if start > len(string) - 1:
        res.append(list(l))
        return
    #for循环继续分割
    for index in range(start+1, len(string)+1):
        strings = string[start:index]
        if isPlalind(strings):
            cut_plalindString(index, string, l+[string[start:index]], res)

def func(string):
    res = []
    cut_plalindString(0, string, [], res)
    return res

print(func("abb"))
'''
Output result：
    [['a', 'b', 'b'], ['a', 'bb']]
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
2、格式化字符串进阶
    给定一个字符串string，检查是否可以重新排列组合成新的字符串，使其满足如下条件：相邻的字符不相同。
如果可以，则返回任意可行的结果即可，如果不可，则返回False。例如：输入字符串：AABBCC，返回：ABCABC
其中一种可行的答案即可。
解题思路：只需找出字符串中字母个数最多的那个，如果其满足：不大于字符串长度+1除以2，则说明可以组成相邻
字符不相同的新的字符串；否则返回False即可。
步骤：
（1）将原字符串中的每个字符个数分别统计出来。将统计完成的结果按照字符串出现的次数从大到小进行排序，
组成数据源列表；
（2）从数据源列表中依次取值填充到新的空列表中，填充列表时：先将偶数位全部填充完成，再填充奇数位；
（3）将新的列表重新组合成最终的结果字符串即可。
'''

def formatString_adv(string):
    dic = {}
    #结果列表先用0填充
    res = ["0" for i in  range(len(string))]
    for i in string:
        #从字典中依次取出元素
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    #dic.item()方法将字典元素返回列表，并以lambda表达式以元素个数返回子列表
    #s="AAABBCC"：[[A:3], [B:2], [C:2]]
    l = sorted(dic.items(), key=lambda x : x[1])
    #最多字符串大于字符串长度+1除以2的情况
    if len(l[-1]) > (len(string)+1) / 2:
        return False

    tempCount = 0   #插入字符个数
    tempItem = None #插入的字符
    #偶数位填充
    for i in range(0, len(string), 2):
        if tempItem == None:
            tempItem = l.pop()  #取出最后一个字符
        #填充偶数位第一个元素
        if tempCount == 0:
            tempCount= tempItem[1]
        res[i] = tempItem[0]
        tempCount -= 1
        #循环插入元素
        if tempCount == 0:
            tempItem = None
    #奇数位填充
    for i in range(1, len(string), 2):
        if tempItem == None:
            tempItem = l.pop()
        if tempCount == 0:
            tempCount = tempItem[1]
        res[i] = tempItem[0]
        tempCount -= 1
        if tempCount == 0:
            tempItem = None
    return "".join(res)

print(formatString_adv("AAABBCCCDDFFF"))
'''
Output result：
    FAFAFDCDCBCBA
'''
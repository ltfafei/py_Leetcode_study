#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
10、查找常用字符串
    现在输入一组字符串，要求编写程序，将其中的常用字符串找出来，常用字符自定为：所输入的一组字符串
中，所有的字符串中都包含此字符，则此字符就被定义为常用字符。例如，输入一组字符串为["XALL", "ABCD",
"APPLE"]，则最终返回["A"]。注意：返回的结果中不能存在重复的字符。
解题步骤：
（1）找到所有字符串中都包含的字符；
（2）进行字符的去重（集合）。
'''

def findGenStr(L):
    box = set(L[0])
    #遍历字符串
    for i in  range(1, len(L)):
        s = L[i]
        temp = set()
        #如果当前字符在box，就添加到临时集合中
        for c in s:
            if c in box:
                temp.add(c)
        box = temp
    return list(box)

print(findGenStr(["XALL", "ABCD", "APPLE"]))
'''
Output result：
    ['A']
'''
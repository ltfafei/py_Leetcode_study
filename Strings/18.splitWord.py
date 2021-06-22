#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
18、拆分单词
    输入一个非空字符串，其中只包含26个英文字母。同时再输入一组单词列表，要求通过编程判断是否可以将输入的字符串
进行拆分，每一部分都是单词列表中的单词。例如输入字符串：helloafei，输入单词列表["hello", "afei"]，则返回True，
如果输入字符串为：looknow，输入单词列表["look", "know"]，则返回False，因为无论先拆出哪个单词，剩下的部分都无法
满足要求。
解题思路：
（1）定义递归函数，输入index作为字符串截取的起点，输入s参数为原字符串；
（2）递归函数输入的index作为起点进行遍历，从前往后遍历过程中，如果能够组成列表中的单词，则再次调用递归函数验证
之后的字符串是否满足要求；
（3）递归结束的条件为当递归函数输入的起点应超过字符串的下标值；
（4）当最外层的遍历结束后，依然没有找到符合条件的场景，则返回False。
'''

def splitCount(s, dic):
    #递归函数
    def breakFunc(start):
        if start >= len(s):
            return True
        for index in range(start+1, len(s)+1):
            #分割
            string = s[start:index]
            #后半部分验证
            if string in dic:
                return breakFunc(index)
        return False
    return breakFunc(0)

print(splitCount("helloafei", ["hello", "afei"]))
'''
Output result：
    True
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
1、格式化字符串
    假设给定一个数字+字母组合的字符串，要求通过编程对字符串进行格式化，使其组成的新的字符串
满足以下条件：
（1）相同类型的字符不能相连，即：数字的左右必须是字母，字母的左右必须是数字；
（2）如果无法满足添加1，则返回False。例如：输入af00e12i3，返回结果3i2e1f0a0

解题思路：
（1）由于数字型的字符有限，只有0-9共10个。首先需要做的就是将字符串中的字符进行分类，可以创建
一个列表，将所有数字型字符放入其中作为分类标准。
（2）字符分完类后，接下来需要进行重新组合，组合需要满足：如果两类字符串的数量差距大于1，则其
一定不能满足题目的要求组成的新的字符串，直接返回False，如果两类字符串的数量差距不大于1，则依次
从两类字符串中取出字符排列组成符合要求的新的字符串即可。注意：首个字符需从字符较多的一类中取。
'''

def formatStrings(s):
    nums = []   #存放数字类
    chars = []  #存放字母类
    #将数字类的10种字符放入列表内
    l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    res = ""
    for i in s:
        #将字符串处理分类
        if i in l:
            nums.append(i)
        else:
            chars.append(i)
    #两类字符数量差大于1的情况
    if abs(len(nums) - len(chars)) > 1:
        return False
    # 数字类较多的情况
    elif len(nums) > len(chars):
        for i in range(0, len(chars)):
            res += nums.pop()
            res += chars.pop()
        res += nums.pop()
    # 数字类和字母类相等的情况
    elif len(nums) == len(chars):
        for i in range(0, len(chars)):
            res += nums.pop()
            res += chars.pop()
    # 字母类较多的情况
    else:
        for i in range(0, len(nums)):
            res += chars.pop()
            res += nums.pop()
        res += chars.pop()
    return res

print(formatStrings("af00e12i3"))
'''
Output result：
    3i2e1f0a0
'''
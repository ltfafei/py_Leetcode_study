#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
11、字符串平移
    定义：字符串平移是指将字符串最左边的字符移动到最右边，其他位置的字符保持不变。现在，输入两个字符串
要求通过编程判断第二个字符串是否可以由第一个字符串平移得到。例如输入：HELLO和LLOHE，则结果返回True。
因为将HELLO，第一次平移得到ELLOH，第二次平移即可得到LLOHE。
'''

def strTranslation_1(s1, s2):
    #第一个字符串为空的情况
    if len(s1) == 0 and len(s2) != 0:
        return False
    #两个字符串长度不相等的情况
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    tmp = s1
    #循环遍历进行平移
    for i in  range(0, len(s1) - 1):
        #从第二个字符截取到最后并且在最后拼接第一个字符，完成一次平移
        tmp = tmp[1:] + tmp[0]
        if tmp == s2:
            return True
    return False

print(strTranslation_1("HELLO", "LLOHE"))
'''
Output result：
    True
'''

'''
进阶：
    需要判断字符串s2是否可以通过字符串s1平移得到，从另一方面看，其实就是将s2字符串扩展一倍后，
s1字符串是否是s2的子串。例如：s1 = HELLO，s2 = LLOHE，s1扩展一倍后就是：HELLOHELLO，s2一定是
s1的子串。
'''

def strTranslation_2(s1, s2):
    return len(s1) == len(s2) and s2 in s1 * 2

print(strTranslation_2("HELLO", "LLOHE"))
'''
Output result：
    True
'''
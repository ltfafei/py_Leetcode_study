#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
31、实现IP模糊匹配
    使用正则表达式中的？和*实现模糊匹配，？代表陪陪单个通配符，*表示匹配任意通配符，即可以匹配任意的字符串。现在，
输入一个字符串和一个匹配模式，尝试编程实现这两个通配符的功能。注意：输入的字符串只包含a-z的26个字母，且都是小写，
例如：输入字符串abcd，和匹配模式ab，需要返回False，输入字符串afff，和匹配模式?fff，需要返回True；同样，输入字符串
abcd和匹配模式*，也需要返回True。注意：*也可以匹配空字符串。
'''

#匹配函数
def match(s, p):
    newS = str(s)
    newP = str(p)
    for c in p:
        #匹配模式不为*情况
        if c != "*":
            if len(s) == 0:
                return False
            #已匹配上的情况
            if c == newS[0] or c == "?":
                newS = newS[1:]
                newP = newP[1:]
            else:
                return False
        #匹配模式为*情况
        else:
            #决策递归进行匹配
            for i in range(len(newS)+1):
                #匹配上
                if match(newS[i:], newP[1:]):
                    return True
            break
    if len(newS) == 0 and len(newP) == 0:
        return True
    return False
#入口函数
def ipFuzz_match(s, p):
    newP = ""
    tmp = ""
    #将重复的*进行合并，提高效率
    for c in p:
        if c == "*" and c == tmp:
            continue
        tmp = c
        newP += tmp
    return match(s, newP)

print(ipFuzz_match("afei", "a*"))
'''
Output result：
    True
'''
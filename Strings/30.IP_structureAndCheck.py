#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
30.1、构建IP地址
    输入一个字符串，其是一组数字。要求将其拆分成一个有效的IP地址，IP地址的每个数中间使用”.“进行分割（点分十进制
表示法）。要求通过编程拆出所有的IP地址并返回，如果不能构成正确的IP地址，则返回空列表。例如：输入：15525511125，需要
输出返回["155.255.111.25", "155.255.11.125"]
解题思路：
（1）编写一个递归函数对字符串进行处理，输入一个要处理的字符串和一个列表，列表中存放当前已经截取出的数字。如果当前要处理
的字符串长度为0，则表明已经处理完成，将列表进行记录；如果当前字符串长度不为0，且列表中已经有4个数字，则表明此条处理路径
无法满足要求，抛弃掉结果；
（2）进行决策，对于当前字符串处理有三条路径，第1个字符单独作为一个数值进行截取，前2个字符作为数值进行截取，前3个字符作为
一个数值进行截取。在决策时，还要处理一些剪枝条件，例如：要处理的字符串长度是否满足，截取的数值是否有前置0，对于3位数，
还要额外判断其是否大于255，之后再进行递归运算。
（3）通过上面的处理，已经将所有的构建情况进行了枚举，由于一个有效的IP地址只能是4个数值，且中间使用“.”进行连接，最终对
结果列表进行整理后返回即可。
'''

def ip_struct(s):
    res = []  #存放结果
    def select(string, l):
        if len(string) == 0:  #已经拆分完
            if len(l) == 4:
                res.append(l)
            return
        if len(l) >= 4:
            return
        # 只拆第一个字符
        m = string[0]
        newL = list(l)
        newL.append(m)
        select(string[1:], newL)
        # 前两位进行拆分
        if len(string) > 1:
            m = string[:2]
            newL = list(l)
            newL.append(m)
            select(string[2:], newL)
        # 前三位进行拆分
        if len(string) > 2 and int(string[:3]) <= 255:
            m = string[:3]
            newL = list(l)
            newL.append(m)
            select(string[3:], newL)
    select(s, [])
    finla = []
    #处理用.进行拼接
    for i in res:
        finla.append(".".join(i))
    return finla

print(ip_struct("15525511125"))
'''
Output result：
    ['155.255.11.125', '155.255.111.25']
'''

'''
30.2、验证IP地址的有效性
    现在输入一个字符串，需要判断其是否是IPv4或IPv6地址。IPv4地址是由4个数字组成，其余不会以0开头，且每个数字都在
0-255之间，数字之间使用“.”进行连接。IPv6地址由8组16进制的数字表示，每组之间使用“:”进行连接。输入的字符串中
只有组成IPv4和IPv6的字符，没有其他字符和空格。如果是有效IP地址，返回True，否则返回False。
解题思路：
对于IPv4：使用“.”分割后将会分割出4个子串，所有子串中只包含数字字符，所有子串不能是空子串，除了“0”外，所有子串
不能以0开头，所有子串转成数值要小于256。
对于IPv6：使用“:”分割后将会分割出8个子串，所有子串中只能包含数字和a(A)-f(F)字符，所有子串不能是空子串，所有子串
的长度不大于4。
'''

def ip_struct_Check(s):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    chars = ["a", "b", "c", "d", "e", "f"]
    #IPv4判断
    if "." in s and ":" not in s:
        l = s.split(".")
        #分割4个子串判断
        if len(l) != 4:
            return False
        #判断只能是数字
        for i in l:
            for c in i:
                if c not in nums:
                    return False
            #为空字符串判断
            if i == "":
                return False
            #为0开头判断
            if len(i) > 1 and i[0] == "0":
                return False
            #小于256判断
            if int(i) >= 256:
                return False
        return True
    # IPv6判断
    elif ":" in s and "." not in s:
        l = s.split(":")
        #分割8个子串判断
        if len(l) != 8:
            return False
        #判断只能是数字和a-f字符
        for i in l:
            for c in i:
                if c not in nums and c.lower() not in chars:
                    return False
            #不为空判断
            if i == "":
                return False
            #子串长度不大于4判断
            if len(i) > 4:
                return False
        return True
    return False

print(ip_struct_Check("2001:01b8:791c:0:0:8a97:bd31:477a"))
'''
Output result：
    True
'''
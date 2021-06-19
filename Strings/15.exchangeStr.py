#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
15.1、交换字符
    输入两个字符串，如果通过交换第一个字符串中的两个字符后就可以得到第二个字符串，则表明这两个字符串可以
相互交换，返回True，如果不能转换，返回False。例如：输入ACB和ABC，返回True；输入ABC和ABC返回False，因为至少
需要进行一次交换。
解题思路：
（1）如果两个字符完全相同，则只有字符串中存在重复字符时才满足条件（将重复字符交换一次）；
（2）如果两个字符不同，如要满足条件，则他们的长度需要相同，并且两个字符串中只有两个位置相异(假设为M位和N位)；
（3）判断字符串A和字符串B不同的两位对应的字符是否满足如下条件：A[M] == B[N]，并且A[N] == B[M]。如果满足，则
可以通过一次交换转换。
'''

def exchangeStr_1(A, B):
    if A == B:
        #有重复字符的情况，set()集合去除重复字符
        if len(A) == len(set(A)):
            return False
        else:
            return True
    if len(A) == len(B):
        #m和n记录位置
        m = -1
        n = -1
        for i in range(len(A)):
            #两个字符串不同的场景
            if A[i] != B[i]:
                if m == -1:
                    m = i
                elif n == -1:
                    n = i
                else:
                    return False
        #是否满足交换条件
        if A[n] == B[m] and A[m] == B[n]:
            return True
        return False
    else:
        return False

print(exchangeStr_1("afei", "aief"))
'''
Output result：
    True
'''

'''
13.2、进阶
    现在给定两个字符串A和B。可以对A中的任意字符进行替换，但是需要遵循如下替换规则：
如果替换某个字符串，则所有此字符都需要被替换成相同的字符。需要通过编程判断字符串A是否可以通过字符替换
得到字符串B。例如：输入A为：AFFEI，B字符串为：CDDKJ，则返回True。因为将A字符串中的字符A替换为C，F替换
为D，E替换为K，I替换为J，即可得到字符串B。
解题思路：
（1）输入的两个字符串如果长度不等，则直接返回False；
（2）输入的两个字符串如果长度完全相等，则直接返回True;
（3）将输入的第一个字符串中字符出现的位置进行统计；
（4）使用统计结果对第二个字符串进行验证，如果有位置不对应的情况出现，直接返回False。如果验证成功，
则返回True。
'''

def exchangeStr_2(A, B):
    #长度不等的情况
    if len(A) != len(B):
        return False
    if A == B:
        return True
    #存放统计结果，返回数组格式：{c:[index, index]}
    dic = {}
    #遍历
    for i in range(len(A)):
        c = A[i]
        if c in dic.keys():
            dic[c].append(i)
        else:
            dic[c] = [i]
    #遍历字典元素
    for (char, indeces) in dic.items():
        count = len(indeces)
        c = B[indeces[0]]   #记录当前字符位置
        if B.count(c) != count:
            return False
        temp = B[indeces[0]]
        for index in indeces:
            if B[index] != temp:
                return False
    return True

print(exchangeStr_2("AFFEI", "CDDJK"))
'''
Output result：
    True
'''
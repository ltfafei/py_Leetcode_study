#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
14、数字翻译成字符串
    使用0-25这26个数字分别对应字母A-Z，现在，给定一个由数字组成的字符串，要求通过编程将其翻译为字母串，并将
所有可能的翻译结果结果个数返回。例如：输入12258，其可能结果有：BCCFI、BWFI、MCFI、BCZI和MZI，所以结果返回5。
解题思路：
（1）对当前输入数值进行判断，如果不大于9，则直接返回1；
（2）如果当前数值大于9且不大于25，则直接返回2；
（3）如果当前数值大于25且小于100，则直接返回1；
（4）如果不满足以上3种场景，则进行决策，分为两种可选的情况：每位数字单独翻译或者组合翻译。
'''

def numTrans_str(num):
    n = int(num)
    if n <= 9:
        return 1
    if n <= 25:
        return 2
    if n < 100:
        return 1
    #两位数情况
    if int(num[:2]) < 26:
        #但数字翻译加组合翻译个数
        return numTrans_str(num[1:]) + numTrans_str(num[2:])
    else:
        return numTrans_str(num[1:])

print(numTrans_str("12258"))
'''
Output result：
    5
'''
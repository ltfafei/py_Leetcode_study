#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
1、假设存在一个k位数N，其每一位上的数字的k次幂的总和也是N，那么这个数就是阿姆斯特朗数。
现在给你一个正整数N，让你来判定这个数是否是阿姆斯特朗数，如果是，返回True，如果不是，返回False。
EG：153是一个3位数，且：153=1^3+5^3+3^3 

    阿姆斯特朗数其实是一种自幂数,三位的阿姆斯特朗数又被称为水仙花数。
水仙花数的名字来自于一个凄美的神话故事，美少年纳西索斯苦苦追求自己的倒影最终化作一朵晶莹剔透的水仙花。
之后,纳西索斯的名字(NARCISSUS)就成了“自我欣赏”的代名词，用水仙花数来称呼3位的自幂数，或许要有些描述“自赏”的味道。

有趣的自幂数：
    一位的自幂数又称独身数；
    三位的自暴数又称水仙花数；
    四位的自幂数又称四叶玫瑰数；
    五位的自幂数又称五角星数；
    六位的自幂数又称六合数；
    七位的自幂数又称北斗七星数；
    八位的自幂数又称八仙数；
    九位的自幂数又称九九重阳数；
    十位的自幂数又称十全十美数。

解题思路：
    （1）首先将一个数中的每一位数字提取出来；
    （2）将提取出来的每一位数字与当前数本身的位数进行指数运算并且累加；
    （3）最后比较累加的结果与数字本身是否相同。
'''

def armStrong(N):
    tmp = N
    list = []
    while tmp / 10.0 > 0:
        #取个位数字
        s = tmp % 10
        list.append(s)
        tmp = tmp // 10
    sum = 0
    for item in list:
        sum += item ** len(list)
        #print(item ** len(list))
    if sum == N:
        return True
    else:
        return False

res = armStrong(153)
print(res)

'''
Output result：
    True
'''

#程序优化1
def armStrong2(N):
    #将int转化为字符串
    strN = str(N)
    list = []
    for item in strN:
        list.append(item)
    sum = 0
    for item in list:
        sum += int(item) ** len(list)
    return sum == N

res = armStrong2(100)
print(res)

'''
Output result：
    False
'''

#程序优化2
def armStrong3(N):
    l = list(str(N))
    sum = 0
    for item in l:
        sum = int(item) ** len(l)
    return sum == N

res = armStrong2(153)
print(res)

'''
Output result：
    True
'''
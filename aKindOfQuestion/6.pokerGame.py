#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
6、扑克游戏
    游戏规则：两个人依次从扑克牌中依次取出5张。如果这五张排可以组成顺子，则当前取牌玩家赢得游戏。顺子是指这5张
扑克牌是连续的。现在约定扑克牌中2-10为数字本身，A为1，J为11，Q为12，K为13。大小王都为0，0可以被视为任意数字，需要注意：13为最大值，其后再取到1也不能组成顺子。
    现在，要求编写程序判断输入的一组扑克牌是否为顺子，例如输入[0,0,5,6,7]，可以组成顺子，因为前两个0可以分别看作3和4。
'''

def isStragth(nums):
    tmp = -1  #记录上一个数字，默认为-1表示没有上一个数字
    zeroCount = 0  #记录0的个数
    #对输入的列表进行遍历
    for n in nums:
        if n == 0:  #如果当前数字为0，则进行记录并作特殊处理
            zeroCount += 1  #计算0的个数
        else:
            #没有上一个数字则赋值直接跳过
            if tmp == -1:
                tmp = n
                continue
            #当上一个数字与当前数字刚好连续，则直接跳过
            if n == tmp + 1:
                tmp += 1
                continue
            #当前数字大于上一个数字且不相连，则用0进行补充
            while zeroCount > 0 and n > tmp + 1:
                tmp += 1
                zeroCount -= 1
            if n == tmp + 1:
                tmp += 1
                continue
            return False
    return True

print(isStragth([0,8,0,0,12]))
'''
Output result：
    True
'''
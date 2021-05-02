#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
12、进步数是顺次数的一种扩展，如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是1，
那么这个数就是一个进步数。例如：321是一个进步数，而421不是。
    现在，给定一个范围，尝试编程查找其范围内的所有进步数，并将其由小到大的组成列表返回。
'''

def progressNumber(low, high):
    #存放所有进步数
    l = [0]
    #将所有筛选出来的进步数存放到res中
    res = []
    #定义一个指针
    p = 0
    #将0这个特殊的进步数添加进去
    if low <= 0:
        res.append(0)
    #将一位数的进步数筛选出来
    while l[-1] < 9:
        l.append(l[-1] + 1)
        if l[-1] >= low and l[-1] <= high:
            res.append([-1])
    while l[-1] < high:
        current = l[p]
        if current == 0:
            p += 1
            continue
        #两位以上步阶数进行判断，如果倒数第一位为边界0的话，只能比它大
        if str(current)[-1] == "0":
            nex = current * 10 + int(str(current)[-1]) + 1
            l.append(nex)
            if nex >= low and nex <= high:
                res.append(nex)
        #如果倒数第一位为边界9的话，只能比它小
        elif str(current)[-1] == "9":
            nex = current * 10 + int(str(current)[-1]) - 1
            l.append(nex)
            if nex >= low and nex <= high:
                res.append(nex)
        #如果都没有满足，说明边界在2-8之间
        else:
            nexLeft = current * 10 + int(str(current)[-1]) - 1
            nexRight = current * 10 + int(str(current)[-1]) + 1
            l.append(nexLeft)
            l.append(nexRight)
            if nexLeft >= low and nexLeft <= high:
                res.append(nexLeft)
            if nexRight >= low and nexRight <= high:
                res.append(nexRight)
            p += 1
    return res
print(progressNumber(10,15))

'''
Output result：
    [10, 12]
'''
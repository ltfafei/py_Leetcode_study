#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
1、连点成线
    在一个XY坐标系中有一些点，我们用数组COORDINATES来分别记录它们的坐标，其中
COORDINATES[I] = [X, Y]表示：X为横坐标的点，Y为纵坐标的点。现在需要通过编写程序
判断这些点在该坐标系中是否在同一条直线上。
判断是否在一条直线上：
    只需要判断两点的横纵坐标的斜率是否相同。
斜率：斜率是用来表示一条直线关于坐标轴倾斜的程度。通常用直线上两点的纵坐标只差与
横坐标只差的比值来表示。
x(斜率) = (y2 -y1) / (x2 - x1) 分母不为0
'''

def dotMakelines(l):
    #如果只有一个点的情况
    if len(l) <= 1:
        return True
    #取出两个点
    p1 = l[0]
    p2 = l[1]
    #取出两个点的横坐标和纵坐标
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    ty = (y2 -y1)
    tx = (x2 - x1)
    for i in range(len(l)):
        pn = l[i]
        xn = pn[0]
        yn = pn[1]
        tnx = (xn - x1)
        tny = (yn - y1)
        if ty * tnx != tx * tny:
            return  False
    return True

print(dotMakelines([[0, 0], [1, 1], [2, 3]]))
'''
Output result：
    False
'''
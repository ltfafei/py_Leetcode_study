#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
2、访问所有点的最短时间
    平面上有一组点，它们的位置都有整数的横纵坐标表示，说明在X、Y轴的正方向。在平面上，1秒的时间可以在
X轴或者Y轴上移动一个单位，也可以横纵坐标同时移动一个单位（对角线）。现在，输入这样一组点，要求通过编程
输出按照数组的顺序依次访问这些点需要的最短时间。
'''

def dotShort_time(l):
    p0 = l[0]
    res = 0
    for i in range(1, len(l)):
        p = l[i]
        #当点移动坐标变化的四种情况
        while p[0] != p0[0] or p[1] != p0[1]:
            if p[0] > p0[0]:
                p0[0] += 1
            if p[1] > p0[1]:
                p0[1] += 1
            if p0 < p0[0]:
                p0[0] -= 1
            if p[1] < p0[1]:
                p0[1] -= 1
            res += 1
        return res
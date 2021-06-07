#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
6、绘制矩形
    在应用开发中，页面的绘制是十分重要的。在尺寸有限的页面上合理的布局组件是应用开发者的基本功。
现在，给定一个矩形面积，要求通过编程规划出合理的长和宽。要求如下：
（1）设计的矩形面积必须与输入的面积相等；
（2）宽度要求小于等于长度；
（3）宽度和长度要差距最小。
    编写一个函数，输入为整型面积值，需要输出一个列表，里面存放所规划矩形的长和宽。
例如：输入4，程序应该输出结果[2,2]
'''

import math
def draw_Rectangle(n):
    l = int(math.sqrt(n))   #获取长
    w = l   #定义宽
    #长宽差距最小判断
    while l * w != n:
        if l * w < n:
            l += 1
        else:
            w -= 1
    return [l, w]

print(draw_Rectangle(8))
'''
Output result：
    [4, 2]
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
8、判断圆和矩形是否相交
    将矩形使用列表表示如下：[x1, y1, x2, y2]，其中（x1，y1）表示矩形左下标坐标，（x2, y2）表示矩形右上角坐标。
同样，平面中的圆也可以使用列表表示，如下：[R, X, Y]，其中R表示圆的半径，（X, Y）表示圆心坐标。
    现在，输入一个表示矩形的列表和表示圆形的列表，要求编程判断矩形和圆是否相交或相切（即是否有重叠部分，包括
相切的情况）。
圆和矩形的位置关系有八种：
（1）圆在矩形的左下角：X < x1，Y < y1
（2）圆在矩形的左边：X < x1, Y > y1, Y < y2
（3）圆在矩形的左上角：X < x1，Y > y1
（4）圆在矩形下边：X > x1，X < x2，Y < y1, Y < y2
（5）圆在矩形上边：X > x1，X < x2，Y > y1, Y > y2
（6）圆在矩形的右下角：X > x2，Y < y1
（7）圆在矩形的右边：X > x2, Y > y1，Y < y2
（8）圆在矩形的右上角：X > x2, Y > y2
'''

import math
def circle_rectangleCheck(r, c):
    # 取出矩形坐标
    x1 = r[0]
    y1 = r[1]
    x2 = r[2]
    y2 = r[3]
    # 取出圆的坐标
    cx = c[1]
    cy = c[2]
    cr = c[0]
    # 圆在矩形的左边
    if cx < x1 and cy >= y1 and cy <= y2:
        return cr >= (x1 - cx)
    # 圆在矩形的右边
    elif cx > x2 and cy >= y1 and cy <= y2:
        return cr >= (cx - x2)
    # 圆在矩形的上边
    elif cy > y2 and cx >= x1 and cx <= x2:
        return cr >= (cy - y2)
    # 圆在矩形的下边
    elif cy < y1 and cx >= x1 and cx <= x2:
        return cr >= (y1 - cy)
    # 圆在矩形的左上角
    elif cy > y2 and cx < x1:
        # 利用勾股定理求圆的半径
        res = ((x1 - cx) * (x1 - cx)) + ((cy - y2) * (cy - y2))
        n = math.sqrt(res)
        return  cr >= n
    # 圆在矩形的左下角
    elif cy < y1 and cx < x1:
        res = ((x1 - cx) * (x1 - cx)) + ((y1 - cy) * (y1 - cy))
        n = math.sqrt(res)
        return cr >= n
    # 圆在矩形的右上角
    elif cy > y2 and cx > x2:
        res = ((cy - y2) * (cy - y2)) + ((cx - x2) * (cx - x2))
        n = math.sqrt(res)
        return cr >= n
    # 圆在矩形的右下角
    elif cy < y1 and cx > x2:
        res = ((y1 - cy) * (y1 - cy)) + ((cx - x2) * (cx - x2))
        n = math.sqrt(res)
        return cr >= n

print(circle_rectangleCheck([0,0,1,2], [1,2,2]))
'''
Output result：
    True
'''
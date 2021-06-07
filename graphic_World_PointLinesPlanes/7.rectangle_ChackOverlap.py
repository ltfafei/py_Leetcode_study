#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
7、判断矩形是否重叠
    平面上的矩形可以使用列表进行表示，例如：[X1, Y1, X2, Y2]，其中（X1，Y1）表示矩形左下角
坐标，(X2, Y2)表示矩形右上角坐标，如果两个矩形有相交的面积，则称两个矩形有重叠。注意：共享
同一条边的两个矩形不算相交。
    现在输入两个列表，分别表示两个矩形，要求通过编程返回这两个矩形是否有重叠。
解题方法：直接通过编程判断两个矩形是否有重叠有难度。可通过判断不重叠解决
判断场景：
  3 *********** 2
    *         *
  0 *********** 1
（1）第2个矩形区域完全在第一个矩形区域左边，这时第2个矩形右上角的横坐标不大于第1个矩形左下角
点的横坐标；
（2）第2个矩形区域完全在第1个矩形区域右边，这时第2个矩形左下角的横坐标不小于第1个矩形右上角
点的横坐标；
（3）第2个矩形区域完全在第1个矩形区域上边，这时第2个矩形左下角的纵坐标不小于第1个矩形右上角
点的纵坐标；
（4）第2个矩形区域完全在第1个矩形区域下边，这时第2个矩形右上角的纵坐标不大于第1个矩形左下角
点的纵坐标。
'''

def rectangle_CheckOverlap(l1, l2):
    #坐标以逆时针标记，情况1判断
    if l2[2] <= l1[0]:
        return False
    #情况2判断
    if l2[0] >= l1[2]:
        return False
    # 情况3判断
    if l2[1] >= l1[3]:
        return False
    # 情况4判断
    if l2[3] <= l1[1]:
        return False
    return True

print(rectangle_CheckOverlap([1, 1, 3, 2], [0, 0, 2, 3]))
'''
Output result：
    True
'''
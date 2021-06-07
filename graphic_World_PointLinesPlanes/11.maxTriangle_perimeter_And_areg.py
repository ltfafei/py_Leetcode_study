#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
11.1、计算三角形最大周长
    输入一个列表l，列表中存放一组数字，表示三角形的边长，要求通过编程找到并计算其中
可组成的三角形中最大的三角形的周长。
三角形特性：
（1）两边之和大于第三边；
（2）两边之差小于第三边。
'''

def countMax_TrianglePerimeter(l):
    l.sort(reverse = True)  #从大到小排序
    #从列表中取出三条边
    for i in range(0, len(l) - 2):
        n1 = l[i]
        n2 = l[i+1]
        n3 = l[i+2]
        if n2 + n3 > n1:
            return n1 + n2 + n3
    return 0

print(countMax_TrianglePerimeter(([3,2,5,4])))
'''
Output result：
    12
'''

'''
11.2、计算最大三角形的面积
    输入一个二维列表，列表中的每个元素都是一个描述点的列表，如[x,y]。从中任取三个点组成一个三角形
要求通过编程找到其中可以组成的最大三角形，并将其面积计算返回结果。例如：输入的列表为：[[0,0],
[0,1], [1,0], [0,2], [2,0]]时，其结果输出为2，因为[[0,0], [0,2], [2,0]]这三个点组成的三角形面积
最大。

巧用海伦公式解题：
    海伦公式最初由古希腊学家阿基米德提出，后来在数学家海伦的著作中给出了公式的证明方法，因此后来人们
更习惯使用海伦的名字来命名这个公式。其实，我国宋代的数学家秦九昭在公元1247年也独立提出了三斜求积术，
其与海伦公式是完全等价的。海伦公式有时也被称为海伦-秦九昭公式。
海伦-秦九昭公式：
S = math,sqrt(p * (p-a) * (p-b) * (p-c))
其中：P为三角形周长的一半，a、b、c分别为三角形的三边长。
'''

import math
def countMaxTriangle_areg(points):
    res = 0
    #取出三角形的三个点
    for i in range(0, len(points) - 2):
        p1 = points[i]
        for j in range(i+1, len(points) - 1):
            p2 = points[j]
            for k in range(j+1, len(points)):
                p3 = points[k]
                #勾股定理计算三角形的三边长
                a = math.sqrt((p2[1] - p1[1]) * ((p2[1] - p1[1])) + (p2[0] - p1[0])* (p2[0] - p1[0]))
                b = math.sqrt((p3[1] - p1[1]) * (p3[1] - p1[1]) + (p3[0] - p1[0]) * (p3[0] - p1[0]))
                c =  math.sqrt((p3[1] - p2[1]) * (p3[1] - p2[1]) + (p3[0] - p2[0]) * (p3[0] - p2[0]))
                p = (a + b + c) / 2
                s = math.sqrt(abs(p * (p-a) *(p-b) * (p-c)))
                if s > res:
                    res = s
    return res

print(countMaxTriangle_areg([[0,0], [1,0], [0,1], [0,2], [2,0]]))
'''
Output result：
    1.9999999999999993
'''
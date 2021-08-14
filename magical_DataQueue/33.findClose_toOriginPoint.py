#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
33、寻找最接近原点的N个点
    平面上有一组点，可使用二维列表来描述这一组点。现在要求编程找出其中距离原点(0,0)最近的N个点。例如：
输入的一组点为：[[1,1], [0,1], [2,1], [0,2]]，输入的N为2，则需要返回[[1,1], [0,1]]，返回的点的顺序不做
限制。
解题思路：
（1）定义一个描述点的类，使用勾股定理将每个点到原点的距离都计算出来；
（2）重载一个小运算符的类用于对堆进行排序；
（3）最后依次取出N个点既是需要的答案。
'''
#定义描述点的类
class Point:
    def __init__(self, point, distance):
        self.point = point  #点
        self.distance = distance  #距离
    #重载小运算符
    def __lt__(self, other):
        return self.distance < other.distance

import heapq  #用于构建堆
import math   #用于勾股定理计算距离

def findClose_toOrigin(l, n):
    heap = []  #存放数据
    #对列表进行遍历
    for i in l:
        #创建模型对象，计算到原点的距离，并将对象压入栈中
        heapq.heappush(heap, Point(i, math.sqrt(i[0] * i[0] + i[1] * i[1])))
    res = []
    #构造小根堆，依次从堆中取出元素，_表示匿名变量
    for _ in range(n):
        res.append(heapq.heappop(heap).point)
    return res

print(findClose_toOrigin([[1,1], [0,1], [2,1], [0,2]], 2))
'''
Output result：
    [[0, 1], [1, 1]]
'''
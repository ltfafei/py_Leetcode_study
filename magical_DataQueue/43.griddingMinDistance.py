#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
43、网格中的最近距离（扩散法）
    现有一张n*n的网格，网格中的每个格子都将存放一个数值0或1。在网格中,任意两个格子的距离可以表示为
|x0 - x1| + |y0 - y1|，现在需要找到一个存放这个数值0个格子，使得这个格子距离最近的存放1的格子的距离
最大，要求使用编程返回此最大距离。
注意：网格以二维表的方式进行输入，其中每个子列表表示一行数据，网格的左上角坐标为(0,0)，向右X轴增大，
向下Y轴增大。例如输入[1,0,0], [0,0,0], [0,1,0]，构建如下表格：
---------------------------------
|    0      |    0    |    0     |
---------------------------------
|    1     |   0    |     0     |
--------------------------------
|    0    |    1   |     0     |
-------------------------------
其中，坐标点(2, 0)的格子满足要求，其距离最近的存放1的格子的距离最大，为3。
解题思路：
    实际上可以让每个存放0的格子都增加1个“距离属性”，此距离表示当前格子与距离最近的存放1的格子的
距离。因此可以采用扩散法。
（1）首先定义一个抽象的模型，为每个格子对象添加“距离”属性，此距离是指其离最近的存放数据1的格子
的距离；
（2）找到所有存放1的格子的对象，向其上下进行扩散，每一轮扩散，距离自增，直到所有需要计算距离的格子
都计算完成为止。
'''

#定义抽象格子模型
class Point:
    def __init__(self, value, p):
        self.value = value  #格子存放的值
        self.p = p      #格子对应的坐标
        self.step = None  #距离
#入口函数，输入n*n列表
def maxGridDistance(grid) -> int:
    allPoint = []  #列表存放Point对象
    all0 = []  #存放所有0的格子
    maxIndex = len(grid) - 1   #n*n列表的下标最大值
    #循环构建格子对象
    for x in range(len(grid)):
        row = grid[x]
        rowL = []
        for y in range(len(row)):
            item = row[y]
            rowL.append(Point(item, [x, y]))
            if item == 1:
                all0.append(Point(item, [x, y]))
        allPoint.append(rowL)
    #该函数用于判断当前格子对象四周是否还有未计算距离的格子
    def countGrid(point):
        x = point[0]
        y = point[1]
        #对应上下左右格子距离计算
        if x > 0:
            item = allPoint[x-1][y]
            if item.step == None:
                return True
        if y > 0:
            item = allPoint[x][y-1]
            if item.step == None:
                return True
        if x < maxIndex:
            item = allPoint[x+1][y]
            if item.step == None:
                return True
        if y < maxIndex:
            item = allPoint[x][y+1]
            if item.step == None:
                return True
        return False
    #计算距离（递归）
    def countDistance(li, dis):
        nexLi = []
        for item in li:
            p = item.step
            x = p[0]
            y = p[1]
            if x > 0:
                ori = allPoint[x-1][y]
                if ori.step == None:
                    ori.step = dis + 1
                if countGrid(ori):
                    nexLi.append(ori)
            if y > 0:
                ori = allPoint[x][y-1]
                if ori.step == None:
                    ori.step = dis + 1
                if countGrid(ori):
                    nexLi.append(ori)
            if x < maxIndex:
                item = allPoint[x + 1][y]
                if ori.step == None:
                    ori.step = dis + 1
                if countGrid(ori):
                    nexLi.append(ori)
            if y < maxIndex:
                item = allPoint[x][y + 1]
                if ori.step == None:
                    ori.step = dis + 1
                if countGrid(ori):
                    nexLi.append(ori)
        #如果还存在未计算距离的格子，则进行递归计算
        if len(nexLi) > 0:
            countDistance(nexLi, dis+1)
    #为所有需要计算距离的格子进行距离计算
    countDistance(all0, 0)
    res = []
    #将所有符合要求的格子的距离遍历出来
    for x in range(len(allPoint)):
        row = allPoint[x]
        for y in range(len(row)):
            p = row[y]
            if p.value == 0 and p.step != None:
                res.append(p.step)
    if len(res) == 0:
        return -1
    #将最大距离返回
    return max(res)
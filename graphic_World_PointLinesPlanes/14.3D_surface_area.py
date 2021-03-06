#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
14、计算三维形体表面积
    在一个平面坐标系上摆放一些长、宽、高都为1的立方体，要求通过编程计算这些立方体组成的三维形体的表面积。
注意：这些立方体都是相接的，不会出现独立的两部分三维形体。现在输入一个二维列表，列表中的每个元素都是一个
列表，用来描述立方体的摆放位置，假设输入的列表为L，其中任一元素C=L[i][j]，即表示在平面坐标(i, y)上摆放
C个立方体。例如：输入L=[[2]]，表示在坐标(0,0)位置垂直摆放2个立方体，其表面积为10；输入L=[[1,2],[3,4]]，
表示在(0,0)位置摆放1个立方体，在(0,1)位置摆放2个立方体，在(1,0)位置摆放3个立方体，在(1，1)位置摆放4个
立方体，其表面积为34。

解题思路：
（1）将每个位置放置的立方体的表面积进行相加；
（2）对位置相邻的立方体，将其接触的表面积减去。
'''

def surface_area(L):
    res = 0
    # 循环x轴，把每一列取出
    for i in range(0, len(L)):
        column = L[i]
        #将每一列的每个元素取出
        for j in range(0, len(column)):
            item = column[j]
            if item > 0:
                #表面积求和
                res += (item * 4 +2)
            #减去每一列重叠的面，上下判断
            if j > 0:
                res -= min(item, column[j-1]) * 2
            # 减去每一行重叠的面，左右判断
            if i > 0:
                res -= min(item, L[i-1][j]) * 2
    return res

print(surface_area([[1,2], [3,4]]))
'''
Output result：
    34
'''
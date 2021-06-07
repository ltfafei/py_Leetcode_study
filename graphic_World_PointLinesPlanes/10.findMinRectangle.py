#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
10、找到最小面积的矩形并计算面积
    输入一个二维列表，其中以列表的形式存放的是一组点坐标，要求通过编程确定由这些点组成的矩形中，
面积最小的矩形是哪个，并将最小面积返回。在构造矩形时，需要满足矩形的边与坐标系的X轴或Y轴平行。
例如：输入[[1,1], [1,3], [3,1], [3,3], [2,2]]这些点，程序执行后返回4。因为这些点组成的最小矩形为
[[1,1], [1,3], [3,1], [3,3]]（分别为矩形的左下角点、左上角点、右下角点和右上角点），矩形面积为4。

思路：
    首先需要找到一种算法来将这些点能够组成的矩形找出。确定一个矩形只需要两个对角线上的点即可。
可以通过遍历列表中的所有的点，两两进行组合，通过这一组合确定一个唯一的矩形，之后检查矩形另外
两个顶点是否在列表内，如果在，则表明可以组成完整的矩形，然后计算其面积，最终通过比较找到
最小面积即可。
'''

def countMinRectangle_areg(points):
    s = 0
    for i in range(0, len(points) - 1):
        #取出第一个点
        p1 = points[i]
        for j in range(i+1, len(points)):
            #取出第二个点
            p2 = points[j]
            #两点在同一条直线上的情况
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue
                #取平均值计算面积
            ss = abs(p2[1] - p1[1]) * abs(p2[0] - p1[0])
            if s > 0 and ss >= s:
                continue
            #确定第三第四个点坐标
            p3 = [p2[0], p1[1]]
            p4 = [p1[0], p2[1]]
            #排除p3、p4不在列表中的情况
            if (p3 not in points) or (p4 not in points):
                continue
            s = ss
    return s

print(countMinRectangle_areg([[1,1], [1,3], [3,1], [3,3], [2,2]]))
'''
Output result：
    4
'''

'''
10.1、最小矩形面积进阶
    现在，去掉：在构造矩形时，需要满足矩形的边与坐标系的X轴或Y轴平行，条件这一条件
对构造的矩形不做任何要求，尝试通过编程找到这些矩形中的最小面积。
问题难点：
（1）现在去掉这一条件意味着对角线的两点可以平行X轴和Y轴；
（2）如何确定哪些点可以组成矩形；
（3）如何获取所组成矩形的长和宽。

思路：
（1）将列表中的点两两组合，作为矩形的对角线；
（2）找出对角线长度相同且中点坐标相同的两组点；
（3）两组点中如果没有相同的点，则表明可以构成矩形，这两组点就是矩形的4个顶点。
'''

import math
def countMinRectangle_areg2(points):
    res = 0
    #存放坐标点字典
    centerList = []
    for i in range(0, len(points) - 1):
        p1 = points[i]
        for j in range(i+1, len(points)):
            p2 = points[j]
            #勾股定理计算对角线长度
            l = math.sqrt((p2[1] - p1[1]) * (p2[1] - p1[1]) +
                          (p2[0] - p1[0]) * (p2[0] - p1[0]))
            #获取中心点坐标
            center = [(p2[1] + p1[1])/2, (p2[0] + p1[0])/2]
            #核心查找逻辑
            for item in centerList:
                #取出对角线另外一个点坐标
                center2 = item["center"]
                l2 = item["l"]
                ps = item["points"]
                #中心点相同且长度相同的两条对角线可以组成矩形
                if center2[0] == center[0] and center2[1] == center2[1] and l == l2:
                    #获取4个顶点坐标
                    pp1 = ps[0]
                    pp2 = p1
                    pp3 = ps[1]
                    pp4 = p2
                    #判断是否有重复的顶点
                    if pp1 == pp2 or pp1 == pp4 or pp2 == pp3 or pp3 == pp4:
                        continue
                    #计算矩形的宽
                    width = math.sqrt((pp2[1] - pp1[1]) * (pp2[1] - pp1[1]) +
                                      (pp2[0] - pp1[0]) * (pp2[0] - pp1[0]))
                    #计算矩形的长
                    length = math.sqrt((pp3[1] - pp2[1]) * (pp3[1] - pp2[1]) +
                                       (pp3[0] - pp2[0]) * (pp3[0] - pp2[0]))
                    s = length * width
                    if res > 0 and s < res:
                        res = s
                    elif res == 0:
                        res = s
        centerList.append({"center": center, "l": l, "points": [p1, p2]})
    return res

print(countMinRectangle_areg2([[0,0], [1,3], [3,1], [3,3], [2,2]]))
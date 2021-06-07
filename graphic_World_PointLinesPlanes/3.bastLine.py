#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
3、最佳直线
    输入一个二位列表，里面存放一组点，要求通过编程找到一条直线，使得这条直线穿过的点最多。
对于程序来说，只需要返回这条直线最先穿过的两点在输入列表中的下标即可。例如：输入[0,0], [1,1],
[1,0], [2,0]，正确的返回结果是[0,2]，因为：[0,0], [1,0], [2,0]这条直线穿过了最多的点，最先穿
过的点为[0,0], [1,0]，在列表中表示的下标0和2。
注意：
    设定对于输入的点组，除了组成的与X轴或Y轴平行的直线可能有多条之外，不会产生多条斜率相同
的平行线。
'''

def bastLine(points):
    lines = {}
    for i in range(0, len(points)-1):
        p1 = points[i]
        for j in  range(i+1, len(points)):
            p2 = points[j]
            n = ""
            #与X轴平行的情况
            if p2[1] - p1[1] == 0:
                n = "x" + str(p2[1]) #标记该点
            #与Y轴平行的情况
            elif p2[0] - p1[0] == 0:
                n = "y" + str(p2[0])
            else:
                n = str((p2[1] - p1[1]) / (p2[0] - p1[0]))  #计算斜率
            if n in lines.keys():
                l = lines[n]
                l.append(j) #记录该点坐标
            else:
                l = []
                l.append(i)
                l.append(j)
                lines[n] = l
    #找出斜率最多的点数
    maxCount = 0
    maxN = 0
    for i in lines.keys():
        item = lines[i]
        if len(item) > maxCount:
            maxCount = len(item)
            maxN = i
    return  lines[maxN][0:2]  #返回前两个点的下标

print(bastLine([[0,0], [1,1], [1,0], [2,0]]))
'''
Output result：
    [0, 2]
'''
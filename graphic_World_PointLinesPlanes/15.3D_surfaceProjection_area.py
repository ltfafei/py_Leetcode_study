#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
15、三维形体投影面积计算
    现在从上面、前面和侧面对三维形体进行投影，要求通过编程计算3个投影图形的总面积。例如：
输入列表L=[[2]]时，其上面、前面和侧面对应的投影图形的面积分别为：1、2、2，最终返回结果：5。

解题思路：
（1）对于上面投影，处理比较容易，只需要对二维列表进行遍历，只要摆放了小立方体，都占据一个
单位的投影面积。上面投影面积只需遍历求和即可；
（2）对于前面的投影，其投影面积实际上是由每一列立方体柱中最高的立方体柱决定的。因此，我们
只需要统计每一列立方体柱中最高的前面面积即可；
（3）对于侧面投影面积，与前面投影类似。但是需要找到每一个立方体柱中最高的一个来计算面积。
由于列表的构造特点，获取一列元素很容易，但想要获取一行元素很麻烦；在不改变列表本身构造
规则的情况下，只需要通过使用字典来遍历过程中每一行元素的高度进行存储，保留高度最高的一个
进行面积计算即可。
'''

def surfaceProject_area(L):
    top = 0     #定义上面投影面积
    front = 0   #定义前面投影面积
    right = 0   #定义侧面投影面积
    dic = {}
    for i in range(0, len(L)):
        column = L[i]
        for j in range(0, len(column)):
            item = column[j]
            #上面投影面积计算
            if item > 0:
                top += 1
            #找到每列中最高的立方柱
            if j in dic.keys():
                if item > dic[j]:
                    dic[j] = item
            else:
                dic[j] = item
        front += max(column)
    #侧面计算
    for i in dic.values():
        right += i
    return top + right +front

print(surfaceProject_area([[2]]))
'''
Output result：
    5
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
9、矩形重叠面积
    输入两个描述矩形的列表，即：r1[x1, y1, x2, y2]，r2[x3, y3, x4, y4]，如果这两个矩形有重叠部分，请计算重叠部分的面积大小；如果
没有重叠部分，直接返回0即可。
'''

def rectangleOverlap_areg(r1, r2):
    # 第一个矩形
    r1x1 = r1[0]
    r1y1 = r1[1]
    r1x2 = r1[2]
    r1y2 = r1[3]
    # 第二个矩形
    r2x1 = r2[0]
    r2y1 = r2[1]
    r2x2 = r2[2]
    r2y2 = r2[3]
    #两个矩形完全不相交的四种情况：完全在左边、完全在右边、完全在上边、完全在下边。
    if r1x2 <= r2x1 or r1x1 >= r2x2 or r1y1 >= r2y2 or r1y2 <= r2y1:
        return 0
    #相交情况分别求四条边的最大最小值
    nx1 = max(r1x1, r2x1)
    nx2 = min(r1x2, r2x2)
    ny1 = max(r1y1, r2y1)
    ny2 = min(r1y2, r2y2)
    return (nx2 - nx1) * (ny2 - ny1)

print(rectangleOverlap_areg([-1,1,3,6], [0,-1,10,2]))
'''
Output result：
    6
'''
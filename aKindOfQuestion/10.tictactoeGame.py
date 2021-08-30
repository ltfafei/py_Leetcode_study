#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
10、井字棋游戏
    井字棋是小时候玩的一种游戏。游戏规则很简单：
在一个3*3的网格中，甲乙两人分别使用X和O棋子。甲乙两人轮流将各自棋子放入空格中，只要棋子练成行，
即代表该玩家获胜，三颗棋子练成行的方式横竖斜都行。
    现在输入一组二维列表，列表中记录的是双反落子的位置坐标，例如输入：[[0,0], [1,0], [0,1]
[1,1], [0,2]]，很明显，甲获胜。假设现在甲（X）先开始落子，要求编程计算比赛结果。
解题思路：
    首先可以根据下子过程进行整理，将数据整合成便于判断输赢的格式。可以定义3个列表rows、columns
和dia，分别用来记录每行、每列和两个对角线的落子情况，之后通过对这3个列表的遍历判断当前棋局
的状态。
'''

def tictactoe(moves):
    rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]    #行列表
    columns = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #列列表
    dia = [[0, 0, 0], [0, 0, 0]]  #对角线列表
    isA = True  #标记交替落子
    #将记录的对战情况填充到指定列表中
    for item in moves:
        tip = 0
        #用1表示甲落子，2表示乙落子
        if isA:
            tip = 1
        else:
            tip = 2
        #进行行填充
        rows[item[0]][item[1]] = tip
        #进行列填充
        columns[item[1]][item[0]] = tip
        #进行对角线填充
        if item[0] == 0 and item[1] == 0:
            dia[0][0] = tip
        if item[0] == 0 and item[1] == 2:
            dia[1][0] = tip
        if item[0] == 1 and item[1] == 1:
            dia[1][1] = tip
        if item[0] == 2 and item[1] == 0:
            dia[1][2] = tip
        if item[0] == 2 and item[1] == 2:
            dia[0][2] = tip
        isA = not isA  #切换落子方
    #进行输赢判定，判断是否有连成一行的相同棋子
    for l in rows:
        if l[0] == 1 and l[1] == 1 and l[2] == 1:
            return "甲获胜"
        elif [0] == 2 and l[1] == 2 and l[2] == 2:
            return "乙获胜"
    for l in columns:
        if l[0] == 1 and l[1] == 1 and l[2] == 1:
            return "甲获胜"
        elif [0] == 2 and l[1] == 2 and l[2] == 2:
            return "乙获胜"
    for l in dia:
        if l[0] == 1 and l[1] == 1 and l[2] == 1:
            return "甲获胜"
        elif [0] == 2 and l[1] == 2 and l[2] == 2:
            return "乙获胜"
    for l in rows:
        for i in l:
            if i == 0:  #没有空格
                return "未分出胜负"
    return "平局"

print(tictactoe([[0,0], [1,0], [0,1], [1,1], [0,2]]))
'''
Output result：
    甲获胜
'''
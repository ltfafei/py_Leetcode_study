#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
4、种树问题
    目前一条路上已经种植了一定的数，且每棵树之间的距离一至，现在假设要求还需要种n棵树，
要保证每棵树之间的间距满足要求，这n棵树能否都种下。可以将问题抽象成一个列表，列表中存放
了0和1两种数值，1表示这个位置被种植了数，0表示没有种，间距的要求可以理解为列表中不能存在
两个相邻的1。现在输入一个列表和一个数值n，要求通过编程计算能否将n棵树种植成功。列入输入
列表为[1,0,0,0,1], n=1，则返回Ture，最终种植结果为[1,0,1,0,1]。
'''

def plantTreeQue(flower, n):
    lenth = len(flower)  #获取所有位置
    for i in range(lenth):
        #如果剩余种树个数为0，则直接返回
        if n == 0:
            break
        #如过当前位置已种树，则跳过
        if flower[i] != 0:
            continue
        #进行第一个位置是否可种树的逻辑判断
        if i == 0 and i + 1 < lenth - 1 and flower[i+1] == 0:
            n -= 1
            flower[i] = 1
        #进行最后一个位置是否可种树的逻辑判断
        elif i == lenth - 1 and flower[i-1] == 0:
            n -= 1
            flower[i] = 1
        #进行中间位置是否可种树的逻辑判断
        elif flower[i-1] == 0 and flower[i+1] == 0:
            n -= 1
            flower[i] = 1
    #如果剩余树苗为0，则说明可以种下这么多树
    return n == 0

print(plantTreeQue([1,0,0,1,0,1,0,0,1], 3))
'''
Output result：
    False
'''
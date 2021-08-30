#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
3、套餐组合问题
    一家餐厅提供主食和饮料两类餐品。每个套餐可以任意组合，一筐主食和一款饮品。服务员会提供主食和
饮品两份菜单供顾客选择。现在输入两个列表，第一个列表代表主食菜单价格，第二个列表存储的是所有饮品
的价格，再输入一个数值n，表示顾客可接受的最大套餐价格，要求编程计算顾客有多少种套餐组合方案。
'''

#方法1：暴力遍历
def combinationMeal_1(staple, drinks, n):
    c = 0  #定义组合方式
    for i in staple:
        for j in drinks:
            if i + j <= n:
                c += 1
    return c

print(combinationMeal_1([15,33,38,56], [8,12,15,16], 88))
'''
Output result：
    16
'''

#优化：如果输入的两个列表元素多的话，那么上面的遍历会变得很慢。
#方法2：双指针法优化
def combinationMeal_2(staple, drinks, n):
    c = 0
    #先对两个列表进行排序
    staple.sort()
    drinks.sort()
    j = len(drinks)  #饮品菜单个数
    #对主食菜单进行遍历
    for i in staple:
        #判断是否满足条件，不满足则移动到较小饮品价格
        while j >= 0 and staple[i] + drinks[j] > n:
            j -= 1
        #如果有满足的说明其他情况都满足，直接计算符合要求组合数
        c += j + 1
    return c
print(combinationMeal_2([15,56,38,33], [8,12,15,16], 88))
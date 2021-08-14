#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
9、将列表中的0进行后置（列表重排）
    输入一个整数列表，列表中穿插存入了元素0。要求编写程序，将列表中所有的0后置，同时保持其他元素的顺序不变。例如：
输入列表为[1,3,0,2,0,5]，则需要返回[1,3,2,5,0,0]。
解题思路：
方法一：创建一个新的列表，通过遍历旧的列表，将旧列表中的元素按照新的规则放入新列表完成重排，这种重排方式被称为
非原地重排；
方法二：通过对旧列表的元素进行交换和移动操作实现重排，这种重排方式被称为原地重排。原地重排可以节省不必要的内存
空间，但是需要需要进行额外的元素移动操作，因此其空间效率高但时间效率低。
在实际应用中，根据需求可以选择算法进行重排。
'''

#非原地重排
def willbeListZeroPostition_1(l):
    res = []  #创建新的列表
    zero = 0  #记录0的个数
    #计算0的个数
    for i in l:
        if i == 0:
            zero += 1
        else:
            res.append(i)
    #计算出0的个数后新列表末尾补0
    res += [0] * zero
    return res

print(willbeListZeroPostition_1([1,3,0,2,0,5]))
'''
Output result：
    [1, 3, 2, 5, 0, 0]
'''

#原地重排
def willbeListZeroPostition_2(l):
    #下标进行循环
    for i in range(len(l) - 1):
        item = l[i]
        if item == 0:
            for j in range(i+1, len(l)):
                #进行交换
                if l[j] != 0:
                    tmp = l[j]
                    l[j] = 0
                    l[i] = tmp
                    break  #完成交换，循环终止
    return l

print(willbeListZeroPostition_2([1,3,0,2,0,5]))
'''
Output result：
    [1, 3, 2, 5, 0, 0]
'''
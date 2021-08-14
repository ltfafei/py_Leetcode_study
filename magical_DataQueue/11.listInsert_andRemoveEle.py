#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
11.1、向列表中插入元素
    输入一个递增的整数列表和一个整数，要求通过编程将这个整数插入到列表中的某个位置，使得原来的列表依然是递增序列
注意：需要使用原地插入的方式进行插入，即不创建新的列表，直接在输入的列表上操作。例如：输入列表L为：[1,3,5,8]，输入
的整数为6，则程序运行结束后，原列表L将变成[1,3,5,6,8]
'''

def listInsert(l, n):
     inserted = False  #标记是否已经插入元素
     for i in range(len(l)):
         item = l[i]
         #找到元素插入
         if item > n:
             inserted = True
             l.append(0)  #列表扩容
             #当前位置元素后移
             for j in range(0, len(l)-i):
                 l[len(l)-j-1] = l[len(l)-j-2]
             l[i] = n
             break
     #如果没找到可插入的位置，则追加到列表末尾
     if not inserted:
         l.append(n)
#由于是原地操作，需要这样调用，不能直接print(listInsert([1,3,5,8],6))
l=[1,3,5,8]
listInsert(l,6)
print(l)
'''
Output result：
    [1, 3, 5, 6, 8]
'''

'''
11.2、清除重复元素
    输入一个有序列表，采用原地删除的方式清除列表中的重复元素，注意：不能改变列表的排序情况。例如：输入一个
列表L为[1,2,2,4,6,6,9]，需要输出结果[1,2,4,6,9]
解题方法：
（1）由于列表是有序的，因此重复的元素一定连续出现，定义一个变量记录上一个元素；定义另一个变量记录去重后的列表
长度，用来清除多余的空间；循环遍历列表，当遇到重复的元素时，将其删除，并依次将后续的元素向前移动，循环完成后，
将多余的空间删除即可。
（2）先转换为集合去重，再转回list返回即可。
'''

def listRemove_1(l):
    c = 0   #记录去重后列表的长度
    pre = None   #记录前一个元素
    i = 0   #循环变量
    while i < len(l):
        item = l[i]
        #遍历可以结束情况
        if item == None:
            break
        #遇到重复元素，进行移动操作
        if item == pre:
            for j in range(i, len(l)-1):
                l[j] = l[j+1]  #将后一个元素依次向前移动
            l[-1] = None
        else:
            i += 1
            pre = item
            c += 1
    del l[c:]  #删除末尾多余的None

l=[1,2,2,4,6,6,9]
listRemove_1(l)
print(l)
'''
Output result：
    [1, 2, 4, 6, 9]
'''

def listRemove_2(l):
    l = list(set(l))
    return l

print(listRemove_2([1,2,2,4,6,6,9]))
'''
Output result：
    [1, 2, 4, 6, 9]
'''
#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
24、交换相邻链表节点
    输入一个链表，要求编程对其相邻节点进行交换。例如输入链表：
1—>2—>3—>4—>5—>None
相邻节点交换后返回结果：
2—>1—>4—>3—>5—>None
解题思路：将链表的值取出进行交换即可。
'''

#定义链表
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList(1)
l2 = NodeList(2)
l3 = NodeList(3)
l4 = NodeList(4)
l5 = NodeList(5)
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

def transBorderList(head):
    ori = head  #定义头节点
    tip = False  #是否进行交换标记
    pre = None  #定义上一个节点
    while head != None:
        #如果前面有节点
        if tip:
            #进行交换
            tmp = head.value
            head.value = pre.value
            pre.value = tmp
        tip = not tip  #取反
        pre = head
        head = head.next
    return ori

res = transBorderList(head)
while res != None:
    print(res.value)
    res = res.next
'''
Output result：
    2
    1
    4
    3
    5
'''
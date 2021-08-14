#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: afei

'''
22.1、链表大数和
    对于数值类型，其所能表示的数据大小是有限制的。如果需要进行非常巨大的数字存储。常常会使用字符串、列表或
链表进行存储。现在，使用两个链表存储两个数值，链表中的每个节点从前往后依次对应数值从低位到高位的一位。例如
下面的链表：
2—>5—>8—>None
其数值表示382.现在输入两个链表，要求计算他们的和，并将结果以相同格式的链表返回。注意：在编写程序时，不能
将链表表示的数值转换为整数，因为这个数值可能非常大。
解题思路：
    程序能够进行大数运算在实际场景中是非常重要的，解决本题的核心就是使用最原始的加法运算原理进行两个大数的
求和运算，即：从低位到高位依次遍历出每一位上的数值后进行求和运算，之后记录进位情况，继续对下一位进行运算，
将每一位运算后的结果构建成链表节点接入链表中。
'''

#定义链表
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

l1 = NodeList(2)
l2 = NodeList(5)
l3 = NodeList(8)
l1.next = l2
l2.next = l3

n1 = NodeList(1)
n2 = NodeList(3)
n3 = NodeList(9)
n1.next = n2
n2.next = n3

def listSum(head1, head2):
    newHead = None  #定义新链表头节点
    current = None  #定义新链表尾节点
    tip = 0   #进位标记
    #核心加法原理运算
    while head1 != None and head2 != None:
        i1 = head1.value
        i2 = head2.value
        c = i1 + i2 + tip
        #两位数需要进行进位
        if c > 9:
            tip = int(c / 10)
        #没有进位的情况
        else:
            tip = 0
        if newHead == None:
            newHead = NodeList(c % 10)
            current = newHead
        else:
            current.next = NodeList(c % 10)
            current = current.next
        head1 = head1.next
        head2 = head2.next
    while head1 != None:
        i1 = head1.value
        c = i1 + tip
        if c > 9:
            tip = int(c / 10)
        else:
            tip = 0
        if newHead == None:
            newHead = NodeList(c % 10)
            current = newHead
        else:
            current.next = NodeList(c % 10)
            current = current.next
        head1 = head1.next
    while head2 != None:
        i2 = head2.value
        c = i2 + tip
        if c > 9:
            tip = int(c / 10)
        if newHead == None:
            newHead = NodeList(c % 10)
            current = newHead
        else:
            current.next = NodeList(c % 10)
            current = current.next
        head2 = head2.next
    #最终检查是否有进位
    if tip != 0:
        current.next = NodeList(tip)
    return newHead

h = listSum(l1, n1)
while h != None:
    print(h.value)
    h = h.next
'''
Output result：
    3
    8
    7
    1
'''

'''
22.2、链表重排
    现在输入一个链表，链表的每个节点都存储一个整数值，再输入一个目标整数值，要求通过编程以输入的目标值
为标准对链表进行重排，使得不大于目标值的节点排列在前，大于目标值的节点排列在后。注意：不能改变原链表
的相对位置。例如，输入的链表为：
1—>2—>3—>5—>8—>6—>4
输入的目标值为：5，则最终需要返回一个新的链表为：
1—>2—>3—>5—>4—>8—>6
'''

class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList(1)
l2 = NodeList(2)
l3 = NodeList(3)
l4 = NodeList(5)
l5 = NodeList(8)
l6 = NodeList(6)
l7 = NodeList(4)
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7

def listsOrder(head, targetVal):
    newHead = None  #新链表头节点
    current = None  #当前节点
    ori = head      #原链表头节点
    while head != None:
        #头节点小于目标值
        if head.value <= targetVal:
            #如果头节点定义的头节点，第一次拼接
            if newHead == None:
                newHead = NodeList(head.value)
                current = newHead
            else:
                current.next = NodeList(head.value)
                current = current.next
        head = head.next
    head = ori
    while head != None:
        #头节点大于目标值
        if head.value > targetVal:
            if newHead == None:
                newHead = NodeList(head.value)
                current = newHead
            else:
                current.next = NodeList(head.value)
                current = current.next
        head = head.next
    return newHead

print("链表重排result：")
h = listsOrder(head, 5)
while h != None:
    print(h.value)
    h = h.next
'''
Output result：
    1
    2
    3
    5
    4
    8
    6
'''
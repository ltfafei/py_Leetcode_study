#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
16.1、遍历链表
    输入一个链表，链表的每个节点使用ListNode对象进行描述，要求通过编程将链表中存放的所有值组成列表进行返回。
ListNode类定义如下：
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None
在ListNode对象中，value属性存放当前节点存储的值，next属性存放下一个ListNode节点。
'''

#定义链表
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList(1)  #value=1
l2 = NodeList(2)   #value=2
l3 = NodeList(3)   #value=3
l4 = NodeList(4)   #value=4
head.next = l2
l2.next = l3
l3.next = l4

#遍历链表
def traverseList_1(head):
    res = []  #结果列表，将链表值value添加到列表
    while head != None:
        res.append(head.value)
        head = head.next
    return res

print(traverseList_1(head))
'''
Output result：
    [1, 2, 3, 4]
'''

'''
16.2、逆序链表
    现在要求通过编程将上述链表的值value进行逆序输出。
解题方法：每次遍历出一个元素后，需要将其作为头节点，将之前的头节点拼接到新的头节点之后进行输出。
'''

def traverseList_2(head):
    pre = None  #标记前一个元素
    #对链表进行遍历
    while head != None:
        #暂无头节点，将当前节点作为头节点
        if pre == None:
            pre = NodeList(head.value)
        else:
            #新建一个节点作为头节点，将之前得头节点拼接到新建的节点上
            node = NodeList(head.value)
            node.next = pre
            pre = node
        head = head.next
    return pre

print(traverseList_1(traverseList_2(head)))
'''
Output result：
    [4, 3, 2, 1]
'''
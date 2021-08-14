#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
19、回文链表
    现在输入一个链表，判断其是否是回文链表，如果是，返回True，否则返回False。
回文链表：正序和逆序输出相同。
例如：
1—>3—>2—>3—>1
1—>2—>3—>3—>2—>1
解题思路：将链表转换为列表，再判断回文即可。
'''

#定义链表
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList(1)
l2 = NodeList(2)
l3 = NodeList(3)
l4 = NodeList(3)
l5 = NodeList(2)
l6 = NodeList(1)
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

def palindromLists(head):
    res_lists = []
    while head != None:
        res_lists.append(head.value)
        head = head.next
    return res_lists == res_lists[::-1]

print(palindromLists(head))
'''
Output result：
    True
'''
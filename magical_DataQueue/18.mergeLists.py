#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
18、合并链表
    现在，输入两个有序链表的头节点，要求通过编程将两个链表拼接成一个完整的有序链表返回。例如输入的链表为：
1—>3—>5—>8—>None
2—>3—>4—>7—>None
则拼接完成后需要返回：
1—>2—>3—>3—>4—>5—>7—>8—>None
'''

#定义链表
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

head1 = NodeList(1)  #value=1
l2 = NodeList(3)   #value=3
l3 = NodeList(5)   #value=5
l4 = NodeList(8)   #value=8
head1.next = l2
l2.next = l3
l3.next = l4

head2= NodeList(2)
l2 = NodeList(3)
l3 = NodeList(4)
l4 = NodeList(7)
head2.next = l2
l2.next = l3
l3.next = l4

def mergeLists(head1, head2):
    head = None  #定义头节点
    current = None  #当前链表值
    #head1和head2都不是头节点情况
    while head1 != None and head2 != None:
        it1 = head1.value
        it2 = head2.value
        #it1拼接到it2后
        if it1 < it2:
            if current != None:
                current.next = NodeList(it1)
                current = current.next
            else:
                head = NodeList(it1)
                current = head
            head1 = head1.next
        else:
            if current != None:
                current.next = NodeList(it2)
                current = current.next
            else:
                head = NodeList(it2)
                current = head
            head2 = head2.next
    #head2已经遍历完成情况，直接遍历head1
    while head1 != None:
        if current != None:
            current.next = NodeList(head1.value)
            current = current.next
        else:
            head = NodeList(head1.value)
            current = head
        head1 = head1.next
    while head2 != None:
        if current != None:
            current.next = NodeList(head2.value)
            current = current.next
        else:
            head = NodeList(head2.value)
            current = head
        head2 = head2.next
    return head

l = mergeLists(head1, head2)
while l != None:
    print(l.value)
    l = l.next
    '''
Output result：
    1
    2
    3
    3
    4
    5
    7
    8
'''
#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
21.奇偶链表
    现在输入一个链表，要求通过编程将其进行重构，将奇数位置的节点排列在前，偶数位置的节点排列在后。注意：这里的
奇偶并不是指链表中存储的值的奇偶，而是指列表节点的位置，例如输入以下链表：
0(1)—>1(2)—>2(3)—>1(4)—>3(5)
重新排列，返回新的链表如下：
0(1)—>2(3)—>3(5)—>1(2)—>1(4)
注：括号中注明链表节点的位置(从1开始)
'''

#定义链表
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList(0)
l2 = NodeList(1)
l3 = NodeList(2)
l4 = NodeList(1)
l5 = NodeList(3)
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

def odd_evenLists(head):
    if head == None:
        return None
    #最终需要返回的新的链表头
    nHead = NodeList(head.value)
    current = nHead  #新链表的当前节点
    #奇偶遍历起点
    h1 = head
    h2 = head
    #遍历奇数位节点
    while h1 != None and h1.next != None and h1.next.next != None:
        current.next = NodeList(h1.next.next.value)
        current = current.next
        h1 = h1.next.next
    #遍历偶数位节点
    if h2 != None:
        current.next = NodeList(h2.value)
        current = current.next
    else:
        return nHead.value
    while h2.next != None and h2.next.next != None:
        current.next = NodeList(h2.next.next.value)
        current = current.next
        h2 = h2.next.next
    return nHead.value

print(odd_evenLists(head))
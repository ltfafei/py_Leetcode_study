#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
20.1 环形链表
    环形链表是一种特殊的链表结构，一般情况下，链表都是单向且不闭合的，即链表中任何一个节点都是只有前一个节点的，
也就是说不存在两个NEXT指针指向同一个节点的情况。但是在实际应用中，同一个链表中是可能有多个节点NEXT指针指向同一个
节点的，这时就产生了环形链表。
注意：环形链表并不是指链表中存在值相同的节点，而是指存在多个节点指向同一个节点，并且节点组成圆环关系。只有两个
节点的链表也可以构成环形链表。例如：
head = NodeList(1)
l2 = NodeList(2)
head.next = l2
l2.next = head
如上代码所示的链表便是环形链表，并且没有头节点也没有尾节点，是一个完美的环形链表。现在，输入一个链表，要求通过
编程判断其是否是环形链表。
'''

#定义链表
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList(1)
l2 = NodeList(2)
l3 = NodeList(3)
head.next = l2
l2.next = l3
l3.next = l2

def isAnnularLists_1(head):
    res = []  #存储出现的链表
    #遍历链表判断
    while head != None:
        #如果遍历的当前的链表在存储的列表中
        if head in res:
            return  True
        res.append(head)
        head = head.next
    return False

print(isAnnularLists_1(head))
'''
Output result：
    True
'''

'''
优化：
    上面的代码最大的问题在于创建了一个额外的容器，并且在遍历过程中，每遍历出一个节点都将其加入到了容器
列表中去，这会增加内存消耗。没有有什么方式可以更少的使用额外的内存空间来解决本题？答案是有的，对链表的
遍历过程其实很像一个小球在轨道上移动。可以把环形链表比作环形轨道，如果让两个速度不同的小球从起点开始
进入轨道，那么在未来的某个时刻，两个小球一定会相遇；如果轨道不是环形的，则速度快的小球会先跑完轨道。可以
通过如上场景来定义两个变量，让其以不同的步长来遍历链表，不需要额外的存储空间，即可判断链表是否是环形链表。
'''

def isAnnularLists_2(head):
    h1 = head
    h2 = head
    #设置不同步长进行循环遍历
    while h1 != None and h2 != None and h2.next != None:
        h1 = h1.next
        h2 = h2.next.next
        if h1 == h2:
            return True
    return False

print(isAnnularLists_2(head))
'''
Output result：
    True
'''

'''
20.2、环形链表进阶
    现在，要求通过编程上上面找到的环形链表中的起点找到并返回。例如：上面定义的链表中，
第二个节点就是起点，如果不是，直接返回False即可。
'''

def isAnnularLists_3(head):
    res = []  #存储出现的链表
    #遍历链表判断
    while head != None:
        #如果遍历的当前的链表在存储的列表中，返回起始节点
        if head in res:
            return  head
        res.append(head)
        head = head.next
    return False

print(isAnnularLists_3(head).value)
'''
Output result：
    2
'''
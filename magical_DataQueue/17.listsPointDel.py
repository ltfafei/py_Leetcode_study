#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
17.1、删除链表中的节点
    使用value和next属性定义链表节点。现在输入一个链表的头节点和一个index下标（下标从0开始），要求编写程序删除链表中
指定位置index的节点。注意：对于链表节点的删除，需要将所删除的节点拼接到上一个节点。例如输入链表为：
1—>2—>3—>4—>5—>None
假设要删除index=3的节点，即第四个链表，执行完程序，将输出结果为：
1—>2—>3—>5—>None

解题思路：关键要找到删除链表某个节点的方法。
    对于一个链表来说，如果要删除的节点不是尾节点，则实际上是将后一个节点复制到前一个节点即可；如果删除的节点是尾节点
则将上一个节点的next指针设置为None即可；如果链表中只有一个节点，删除此节点后，直接复制None即可。
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
l5 = NodeList(5)   #value=5
l6 = NodeList(5)   #value=5
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

#删除链表某个节点
def listsPointDel_1(head, index):
    i = 0
    pre = None  #前一个链表
    #当前节点有值判断
    while head != None:
        if i == index:
            #不是尾节点情况
            if head.next != None:
                head.value = head.next.value
                head.next = head.next.next
            #是否是头节点
            elif pre != None:
                pre.next = None
            else:
                return None
        pre = head
        head = head.next
        i += 1

listsPointDel_1(head, 3)  #删除index为3的链表(4)
list_ = []
while head != None:
    #print(head.value)
    list_.append(head.value)
    head = head.next
print(list_)
'''
Output result：
    [1, 2, 3, 5, 5]
'''

'''
17.2、删除链表中的重复节点
    现在，链表定义依旧方法依旧如上，现在要求编程实现删除重复的链表。
解题方法：
（1）首先使用一个容器来记录列表中已经出现的元素，之后对链表进行遍历，遍历过程中如果发现已经存在的元素，则
将其移除，移除的方法和前面所使用的方法一致，需要对所移除的元素是否是尾元素做不同的逻辑。
（2）遍历拼接链表为列表，转换为set()集合去重之后再转回来。
'''

class NodeList2:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList2(1)  #value=1
l2 = NodeList2(2)   #value=2
l3 = NodeList2(3)   #value=3
l4 = NodeList2(4)   #value=4
l5 = NodeList2(5)   #value=5
l6 = NodeList2(5)   #value=5
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

def listsPointDel_2(head):
    l = []  #存放链表中的元素
    pre = None
    while head != None:
        #元素重复的情况处理
        if head.value in l:
            #不是尾节点
            if head.next != None:
                head.value = head.next.value
                head.next = head.next.next
                continue
            else:
                pre.next = None
        #没有重复直接添加
        l.append(head.value)
        pre = head
        head = head.next

listsPointDel_2(head)
while head != None:
    print(head.value)
    head = head.next
'''
Output result：
    1
    2
    3
    4
    5
'''

class NodeList3:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList3(1)  #value=1
l2 = NodeList3(2)   #value=2
l3 = NodeList3(3)   #value=3
l4 = NodeList3(4)   #value=4
l5 = NodeList3(5)   #value=5
l6 = NodeList3(5)   #value=5
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

def listsPointDel_3(head):
    res_lists = []
    while head != None:
        res_lists.append(head.value)
        head = head.next
    return list(set(res_lists))

print(listsPointDel_3(head))
'''
Output result：
    [1, 2, 3, 4, 5]
'''
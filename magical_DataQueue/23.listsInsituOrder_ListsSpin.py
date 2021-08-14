#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
23.1、链表原地排序
    和列表一样，链表也可以进行排序，使用value和next属性描述链表节点。现在输入一个链表头节点，要求通过编程对其
进行原地排序(升序排序)。例如输入的链表为：
3—>9—>7—>5—>1—>None
原地排序后，结果输出为：
1—>3—>5—>7—>9—>None
解题思路：
    可以将每个节点看作一个容器，只需要创建一个新的容器(列表)，将每个容器中的值取出放到新的容器中进行升序排序即可。
'''

#定义链表
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList(3)
l2 = NodeList(9)
l3 = NodeList(7)
l4 = NodeList(5)
l5 = NodeList(1)
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

def listsInsituOrder(head):
    newL = []
    ori = head
    #将链表中的值取出来，放到列表中
    while head != None:
        newL.append(head.value)
        head = head.next
    newL.sort()  #排序
    ori = head
    #重新写入到新列表中
    for i in newL:
        head.value = i
        head = head.next
    return ori

'''
23.2、对链表进行原地排序
    现在定义，链表的旋转是指将最后一个节点转变为头节点，除此之外每个节点统一向后移动一位，
这样的一次操作被称为链表旋转一次。例如：
1—>2—>3—>4—>None
旋转一次后变成：
4—>1—>2—>3—>None
解题思路：
（1）找到当前链表的尾节点与倒数第二个节点；
（2）将尾节点的NEXT指针指向链表的头节点；
（3）将倒数第二个节点的NEXT指针置为NONE。
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

def listsSpin(head, key):
    #空链表或单节点链表直接返回
    if head ==None or head.next == None:
        return head
    ori = head
    #获取链表长度
    i = 0
    while head != None:
        i += 1
        head = head.next
    #优化旋转次数，如果链表个数是奇数，那么旋转3次、6次...都是一样的
    key = key % i  #取余即可
    head = ori
    #定义旋转操作函数
    def Spin(head):
        ori = head
        if head == None:
            return None
        last = None  #尾节点
        pre = None   #倒数第二个节点
        while head.next != None:
            pre = head
            head = head.next
        last = head
        if pre != None:
            pre.next = None
        last.next = ori
        return last
    #根据输入进行旋转
    for i in range(key):
        head = Spin(head)
    return head

res = listsSpin(head, 1)
while res != None:
    print(res.value)
    res = res.next
'''
Output result：
    5
    1
    2
    3
    4
'''
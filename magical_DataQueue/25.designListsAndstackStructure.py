#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
25.1、设计链表
    现在，要求尝试自己设计一个链表存储结构，设计的存储结构需要满足以下要求：
（1）获取链表中第i个节点存储的值（i从0开始），如果索引无效，则返回None；
（2）在链表的第i个节点前插入一个新的节点，并向链表的末尾追加元素；
（3）获取链表中节点的个数，删除链表中第i个节点，并将删除的节点的值返回；
（4）支持使用列表来创建当前链表对象。
注意：需要做一个自定义的链表结构类，使其能够提供满足以上所列出的功能，在设计时，应该尽量使得方法的
运行效率高。
'''

#定义链表节点类
class designLists:
    def __init__(self, value):
        self.value = value
        self.next = None
#链表容器类
class linkedLists:
    #定义构造方法，可以通过列表来初始化
    def __init__(self, L):
        self.length = 0    #链表长度
        self.head = None  #当前链表头节点
        self.tail = None  #当前链表尾节点
        current = None    #当前节点
        #遍历列表，组成链表
        for i in L:
            if current == None:
                current = designLists(i)
                self.head = current
            else:
                current.next = designLists(i)
                current = current.next
        self.tail = current
        self.length = len(L)
    #定义获取链表节点个数的方法
    def countLists(self):
        return self.length
    #定义获取链表某个节点值的方法
    def getValue(self, index: int):
        head = self.head
        i = 0  #计数器
        while head != None:
            if i == index:
                return head.value
            head = head.next
            i += 1
        return None
    #向链表头部插入节点
    def addListHead(self, value: int) -> None:
        self.length += 1
        #如果头节点为空，就创建头节点
        if self.head == None:
            self.head = designLists(value)
            self.tail = self.head
        #否则直接插入即可
        else:
            item = designLists(value)
            item.next = self.head
            self.head = item
    #向链表尾部追加节点
    def addListTail(self, value: int) -> None:
        self.length += 1
        if self.head == None:
            self.head = designLists(value)
            self.tail = self.head
        else:
            self.tail.next = designLists(value)
            self.tail = self.tail.next
    #在链表中的某个位置插入节点
    def addListsIndex(self, index: int, value: int) -> None:
        #说明在尾部，直接调用尾部的插入方法
        if index == self.length:
            self.addListTail(value)
            return
        #说明在头部，直接调用头部插入方法
        if index <= 0:
            self.addListHead(value)
            return
        elif index > self.length:
            return
        head = self.head
        i = 0
        #在中间，找到位置进行插入
        while head != None:
            if i == index - 1:
                item = designLists(value)
                item.next = head.next
                head.next = item
                self.length += 1
                break
            head = head.next
            i += 1
    #删除链表中某个位置的节点
    def deleteListsIndex(self, index: int) -> None:
        head = self.head
        i = 0
        pre = None  #定义上一个节点
        while head != None:
            if i == index:
                #如果改变了头尾节点，需要进行修在
                if pre != None:
                    pre.next = head.next
                    if head.next == None:
                        self.tail = pre
                else:
                    if self.head.next == None:
                        self.tail = None
                    self.head = self.head.next
                self.length -= 1
                return head.value
            pre = head
            head = head.next
            i += 1

'''
25.2、设计栈结构
    现在需要设计一个栈结构，使其支持如下要求：
（1）将元素压入栈中；
（2）取出栈顶得元素；
（3）检索栈中最小元素。
'''

class MinStack:
    def __init__(self):
        self.content = []
        self.min = None
    #入栈方法
    def push(self, i: int) -> None:
        self.content.append(i)
        #分情况处理最小值的更新
        if self.min == None:
            self.min = i
        elif self.min > i:
            self.min = i
    #出栈方法
    def pop(self) -> None:
        t = self.content.pop()
        if len(self.content) == 0:
            self.min = None
        else:
            if t == self.min:
                self.min = min(self.content)
    #取栈顶元素
    def top(self) -> int:
        return  self.content[-1]
    #获取最小值
    def getMin(self) -> int:
        return self.min
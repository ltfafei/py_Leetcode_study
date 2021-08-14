#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
34.1、设计队列
    要求使用编程设计一个队列，满足如下功能：
（1）将元素压入队列的队尾（push）；
（2）获取队列首部元素（item）
（3）移除并返回队列首部元素（pop）
（4）获取队列中元素的个数（count）
（5）获取队列是否为空（empty）
解题思路：使用链表解题
'''

#定义列表节点类
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

#定义队列容器类
class myQueue:
    #实现构造方法， 定义链表首尾指针和链表长度变量
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    #实现队列push方法，将数据加入队尾
    def push(self, x: int) -> None:
        if self.tail == None:
            self.head = NodeList(x)
            self.tail = self.head
        else:
            self.tail.next = NodeList(x)
            self.tail = self.tail.next
        self.count += 1
    #实现队列pop方法，将队列首元素删除
    def pop(self) -> int:
        if self.head != None:
            v = self.head.value
            if self.tail == self.head:
                self.tail = None
            self.head = self.head.next
            self.count -= 1
            return  v
        else:
            return 0
    #获取队列首元素的值
    def peek(self) -> int:
        if self.head != None:
            return self.head.value
        return 0
    #判断队列是否为空
    def empty(self) -> bool:
        return self.count == 0
    #获取队列长度
    def count(self) -> int:
        return self.count

'''
34.2、设计循环队列
    现在，要求编程设计一个循环队列。可以将空间想像成为一个首尾相接的空间。对于循环队列来说，
空间是没有首尾的，通过首尾指针来标记队列的首尾，当循环队列的所有空间都被填满了数据后，则此时
队列为满状态，无法再将新的元素插入。现在要求设计一个循环队列，实现如下方法：
（1）构造方法，通过设置空间最大容量来初始化循环队列；
（2）获取队列首元素的方法（first）
（3）获取队列尾元素的方法（last）
（4）向队列中添加元素（push）
（5）删除队列中的元素，并将其返回（pop）
（6）检查队列是否为空（empty）
（7）检查队列是否已满（full）
'''

#定义节点类
class Node:
    def __init__(self):
        self.value = None  #节点值
        self.next = None   #节点下一个对象
        self.previous = None  #节点上一个对象

#队列类实现
class myCircularQueue:
    def __init__(self, k: int):
        self.tail = None
        self.list = None  #内部链表
        tmpNode = None
        #遍历创建循环链表
        for _ in range(k):
            node = Node()
            if self.list == None:
                self.list = node
            else:
                tmpNode.next = node
                node.previous = tmpNode
            tmpNode = node
        #首尾相接（循环链表）
        tmpNode.next = self.list
        self.list.previous = tmpNode
        self.head = self.list
        self.tail = self.list
    #添加元素方法
    def enQueue(self, value: int) -> bool:
        if self.tail.next == self.head:
            return  False
        if self.head.value == None:
            self.head.value = value
        else:
            self.head.previous.value = value
            self.head = self.head.previous
        return True
    #删除元素方法
    def deQueue(self) -> bool:
        if self.tail.value == None:
            return False
        self.tail.value = None
        if self.head != self.tail:
            self.tail = self.tail.previous
        return True
    #获取头元素
    def Front(self) -> int:
        return self.head.value

    # 获取尾元素
    def Rear(self) -> int:
        return self.tail.value
    #判断队列是否为空
    def isEmpty(self) -> bool:
        return self.head.value == None

    # 判断队列是否已满
    def ifFull(self) -> bool:
        return self.tail.next == self.head
#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
2.1、简单猜数字
    使用随机数生成一个数字，编写一个猜数字游戏。由于数字随机产生，且只有一次猜的机会。
'''
import random
a = random.randint(0,55)
x = input('请输入一个0-55之间的数：')
if x.isdigit():
    x = int(x)
    if x == a:
        print('恭喜你猜对了')
    elif x > a:
        print('高了')
    else:
        print('低了')
    print('这个数是：',a)
else:
    print('你输入的不是整数')
'''
Output result：
    请输入一个0-55之间的数：10
    低了
    这个数是： 12
'''

'''
2.2、简单猜数字
    使用随机数生成一个数字，编写一个猜数字游戏。由于数字随机产生，且只有3次猜的机会。
'''

# 引入random模块,就是专门产生随机数的
import random

# 把我们的random.randint随机数赋值给我们的answer变量
answer =  random.randint(1,100)
print('='*50)
print('欢迎来到猜数游戏')
print('='*50)
print('\n')
num = input('请输入你猜测的数字:')
guess = int(num)
n = 0
while n < 2:
    if guess == answer and n == 0:
        print('恭喜你猜对了')
        print('厉害了，我的天，一次就猜对了')
        break
    if guess < answer:
            print('不对哦，太小了')
    elif guess > answer:
            print('不对哦，太大了')
    elif guess == answer:
        print('Mygod! 猜对了')
    num = input('请重新输入你猜测的数字：\n')
    guess = int(num)
    n += 1
    if n == 1 and guess == answer:
        print('可以哦，第二次就猜对了')
        break
    elif n == 2 and guess == answer:
        print('还可可，终于被你猜出来了')
        break
    elif n == 2 and guess != answer:
        print('不对哦，小兄弟，看来你的道行还不够哦')
        break
print('游戏结束')
'''
Output result：
    ==================================================
    欢迎来到猜数游戏
    ==================================================
    
    请输入你猜测的数字:22
    不对哦，太小了
    请重新输入你猜测的数字：
    33
    不对哦，太小了
    请重新输入你猜测的数字：
    44
    不对哦，小兄弟，看来你的道行还不够哦
    游戏结束
'''

'''
2.3、猜数字游戏-3
    现在，裁判员写下一个0-n的数字，由玩家来猜，如果猜的值偏大，则会告诉猜大了；如果小了就告诉猜小了
直到玩家猜中为止。现在假设定义好了一个guess函数，其输入一个数值x，返回一个数值告知是否猜中，如果猜大了
，则返回1，如果猜小了，则会返回-1，如果猜中了，则会返回0.要求编写一个函数，输入数值n，表示需要猜的数字
在0-n之间，通过调用guess函数来用相对少的次数猜出最终的答案。
解题方法：
    对于猜数字的游戏，只要按顺序依次尝试，一定可以猜出正确答案，最常用的就是二分法。可以极大提高
猜中概率。
'''

def guess():
    ...

def guessNum_3(n):
    l = 0
    h = n
    num = (l + h) // 2
    while guess(num) != 0:
        if guess(num) > 0:
            h = (l + h) // 2 - 1
        else:
            l = (l + h) // 2 + 1
        num = (l + h) // 2
    return num
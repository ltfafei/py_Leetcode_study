#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#Author: afei00123

'''
11、白钱买白鸡问题
    我国古代数学家张丘建在《算经》一书中曾提出过著名的“百钱买百鸡”问题，该问题叙述如下：
鸡翁一，值钱五；鸡母一，值钱三；鸡雏三，值钱一；百钱买百鸡，则翁、母、雏各几何？
翻译过来，意思是公鸡一个五块钱，母鸡一个三块钱，小鸡三个一块钱，现在要用一百块钱买一百只鸡，
问公鸡、母鸡、小鸡各多少只？
'''

import time
#Python 3.8已移除time.clock()方法。可以使用time.perf_counter()或time.process_time()方法替代。

# 方法1：枚举法，分别用x,y,z表示公鸡，母鸡和小鸡的数目
start = time.process_time()
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            if x + y + z == 100 and 5*x + 3*y + z//3 == 100:
                print("公鸡%d只，母鸡%d只，小鸡%d只" %(x, y, z))
end = time.process_time()
# 计算方法1的所用的时间
print(end-start)
print('\n')
'''
Output result：
    公鸡3只，母鸡20只，小鸡77只
    公鸡4只，母鸡18只，小鸡78只
    公鸡7只，母鸡13只，小鸡80只
    公鸡8只，母鸡11只，小鸡81只
    公鸡11只，母鸡6只，小鸡83只
    公鸡12只，母鸡4只，小鸡84只
    0.09375
'''

# 方法二：枚举法，用a,b,c表示钱数
start = time.process_time()
for a in range(5, 101, 5):
    for b in range(3, 101-a, 3):
        for c in range(1, 101-a-b):
            if a + b + c == 100 and a/5 + b/3 + 3*c == 100:
                print("公鸡%d只，母鸡%d只，小鸡%d只" %(a, b, c))
end = time.process_time()
# 计算方法2的所用的时间
print(end-start)
print('\n')
'''
Output result：
    公鸡20只，母鸡54只，小鸡26只
    公鸡40只，母鸡33只，小鸡27只
    公鸡60只，母鸡12只，小鸡28只
    0.0
'''

'''方法三：用d,e,f表示公鸡，母鸡和小鸡的数量,
首先取出可能的最大的公鸡和母鸡数，然后利用
鸡的总数和钱数限制条件，枚举出所有可能的结果。
'''
start = time.process_time()
d_max = int(100/5)
e_max = int(100/3)
for d in range(d_max):
    for e in range(e_max):
        f = 100 - d - e
        if f%3 == 0 and 5*d + 3*e + f/3 == 100:
            print("公鸡{0}只，母鸡{1}只，小鸡{2}只".format(d, e, f))
end = time.process_time()
# 计算方法3的所用的时间
print(end-start)
'''
Output result：
    公鸡0只，母鸡25只，小鸡75只
    公鸡4只，母鸡18只，小鸡78只
    公鸡8只，母鸡11只，小鸡81只
    公鸡12只，母鸡4只，小鸡84只
    0.0
'''
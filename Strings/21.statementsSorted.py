#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
21.1、语句逆序
    输入一个字符串，其描述的一句英文语句。要求通过编程对语句进行逆序输出。注意：字符串中的单词只以空格
进行分割，不需要处理标点符号。例如输入："I love python"，输出结果：python love I
'''

def statementSort_1(sta):
    l = sta.split()
    l.reverse()
    return " ".join(l)

print(statementSort_1("I love python"))
'''
Output result：
    python love I
'''

'''
21.2、语句重排
    输入一个字符串，字符串描述的是一句英文语句。定义字符串中除了单词外只有空格，并且单词是以
空格进行分割，每两个单词间只会使用一个空格进行分割，现在要求编写程序对英文语句进行重排，将较短
的单词排列在前，如果有长度相同的单词出现，则以它们在原字符串中的顺序为准。在进行语句重排时，需要
满足语句句首字母大写的要求。例如输入字符串："Python is very cool"，将输出结果："Is very cool python"
解题思路：
（1）使用空格对字符串进行分割，将单词提取出来；
（2）将单词根据长度进行排序，过程中将首字母大写，其他字母都转成小写。
'''

def statementSort_2(sta):
    l = sta.split()
    res = []   #存放结果
    #遍历列表中的单词
    for i in l:
        insert = False  #定义插入状态
        i = i.lower()
        #遍历索引
        for index in range(0, len(res)):
            w = res[index]
            if len(i) < len(w):
                res.insert(index, i)
                insert = True   #插入成功
                break
        #如果没有插入，直接添加到最后
        if not insert:
            res.append(i)
    #新语句拼接
    newStr = " ".join(res)
    # capitalize()方法将首字母大写
    return newStr.capitalize()

print(statementSort_2("Python is very cool"))
'''
Output result：
    Is very cool python
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
2、自除数是指可以被它包含的每一位数除尽的数，也可以理解为，自除数对组成其本身的
每一位数字进行取余操作，结果都为0，注意：自除数不允许包含0。如：128是一个自除数，
因为：128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

    现在，给定上边界和下边界的数字，输出一个列表，列表的元素是边界(含边界)内所有
的自除数。请尝试解决。
'''

def selfDivisor(left, right):
    l = []
    for num in range(left, right+1):
        numStr = str(num)
        numList = list(numStr)
        res = True
        for item in numList:
            itemNum = int(item)
            #剔除自除数为0的情况
            if itemNum == 0:
                res = False
                break
            #剔除不能自身除尽的情况
            if num % itemNum != 0:
                res = False
        #将自除数添加到列表中
        if res:
            l.append(num)
    return l
    
print(selfDivisor(100, 200))

'''
Output result：
    [111, 112, 115, 122, 124, 126, 128, 132, 135, 144, 155, 162, 168, 175, 184]
'''

#程序优化1
def selfDivisor2(left, right):
    l = [num for num in range(left, right+1) if([item for item in list(str(num)) if (int(item) != 0 and num % int(item) == 0)] == list(str(num)))]
    return l
        
print(selfDivisor2(128, 201))

'''
Output result：
    [128, 132, 135, 144, 155, 162, 168, 175, 184]
'''
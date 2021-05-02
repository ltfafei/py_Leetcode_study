#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
10、对于一个正整数，每一次将该数替换为它每个位置上的平方和，然后重复这个过程直到这个数变为1，
也可能是无限循环但始终变不到1，如果可以变为1，那么这个数就是快乐数，否则就不是。
    例如：19是一个快乐数，证明如下：
    1^2 + 9^2 = 82
    8^2 + 2^2 = 64
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
    
    现在要求编写程序，求输入一个数N，判断其是否是一个快乐数。
'''

def happyNumber(N):
    #定义一个临时列表存放所有拆解的数字
    tmp = [N]
    while N != 1:
        #将输入的数转换为列表
        l = list((str(N)))
        res = 0
        for i in l:
            res += int(i) * int(i)
        #如果res在tmp中，终止循环，说明不是一个快乐数
        if res in tmp:
            return False
        tmp.append(res)
        N = res
    return True
print(happyNumber(91))

'''
Output result：
    True
'''
#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
5、杨辉三角的某一行
    现在输入一个正整数N，要求通过编程输出杨辉三角第N行的元素。
'''

#只需要在上一题的基础上取出最后一行元素即可
def pascal_Aline(N):
    res = []  # 存放输出的二维数组
    for i in range(0, N):
        l = []
        # 第一行，添加1
        if i == 0:
            l.append(1)
        else:
            # 如果不是第一行
            tmp = [0] + res[-1] + [0]  # 左前方和右前方用0替代
            while len(tmp) > 1:
                l.append(tmp[0] + tmp[1])
                del tmp[0]
        res.append(l)
    return res[-1]

print(pascal_Aline(4))
'''
Output result：
    [1, 3, 3, 1]
'''

'''
程序优化：
    其实不需要将所有的杨辉三角的行获取到，再去取出倒数第一个元素，这样降低了程序的性能。
利用杨辉三角的性质解题。
杨辉三角的性质：
（1）每行数字左右对称；
（2）每行数字的起始数字都是1；
（3）第N行的数字有N个；
（4）第N行的第M个数字可以使用组合公式进行表达，即：C(N-1, M-1)。
组合计算方式：
    C(n,m) = n! / (m! * (n-m)!)
所以第n行的第m个元素可以表示为：
    C(n-1,m -1) = (n-1)! / ((m-1)! * ((n-1)-(m-1))!)
那么第n行的第m+1个元素可以表示为：
    C(n-1,m-1+1) = (n-1)! / (m! * ((n-1)-m)!)
第m+1个元素与第m个元素的比值为：
    K = (n-1)! / (m! * ((n-1)-m)!) * (((m-1)! * ((n-1)-(m-1))!) / (n-1)!)
      = (m-1)! * (n-m)! / (m! * (n-1-m)!)
      = (m-1)! * (n-m)! / (m * (m-1)! * (n-m-1)!
      = (n-m)! / (m * (n-m-1)!
      = (n-m) * (n-m-1)! / (m * (n-m-1)!
      = (n-m)/m
'''

def pascal_Aline(n):
    tmp = 1  #第一个元素
    res = []
    for i in range(1, n+1):  #从1循环到n行
        res.append(tmp)
        tmp = tmp * (n - i) // i
    return res

print(pascal_Aline(4))
'''
Output result：
    [1, 3, 3, 1]
'''
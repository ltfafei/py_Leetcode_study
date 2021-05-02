#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
8、定义丑数为只包含质因数2、3和5的正整数，现在，对定义做一个扩展。

    假设输入任意数A、B和C，请找到第N个可以被A或B或C整除的正整数。
例如：
    设定A=2，B=3，C=5，N等于3。此时，符合条件的丑数列表为：[2, 3, 4, 5 ...]
    符合条件的第三个数为：4
解题思路：
（1）查找的范围如何确定；
    查找范围：输入的3个数字A，B和C中的最小数就是要查找的最小边界，最小数乘以N的值
    就是要查找范围的最大边界。
（3）如何确定某个数是第几个丑数。可使用二分法查找第N个丑数。
    根据定义，知道能够被A或B或C整除的数都被定义为丑数，因此对任意一个数X，
    只需要能够确定0-X范围内有多少个丑数即可，即找到0-X范围内所有可以被A整除或
    可以被B整除或可以被C整除的数。
    可能被整除的几种情况：
        1）只能被a整除(X/a);
        2）只能被b整除(X/b);
        3）只能被c整除(X/c);
        4）只能被a和b整除(X/a_b)；
        5）只能被a和c整除(X/a_c);
        6）只能被b和c整除(X/b_c);
        7）能够被a，b和c整除(X/a_b_c)。
        0-X范围内丑数：X/a + X/b + X/c - X/a_b - X/a_c - X/b_c - X/a_b_c
        只能被a和b整除，需要求他们的最小公倍数
'''

def mincomon(a, b):
    n = a * b
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return int(n / a)
#print(mincomon(4, 6))

'''
Output result：
    12
'''

def search_UglyNumber(MIN, MAX, a, b, c, n):
    if MIN >= MAX:
        return MIN
    #找到二分中间点数
    MID = int((MIN + MAX) / 2)
    #求最小公倍数
    ab = mincomon(a, b)
    ac = mincomon(a, c)
    bc = mincomon(b, c)
    abc = mincomon(a, bc)
    #找出0-n范围内丑数
    res = int(MID / a) + int(MID / b) + (MID / c) - int(MID / ab) - int(MID / ac) - int(MID - bc) + int(MID - abc)
    if res == n:
        return MID
    #如果res < n继续查找
    if res < n:
        return search_UglyNumber(MID + 1, MAX, a, b, c, n)
    else:
        return search_UglyNumber(MIN, MID - 1, a, b, c, n)

#使用二分法查找第N个丑数
def N_uglyNumber(a, b, c, n):
    MIN = min(a, b, c)
    #找到最大数的最小范围
    MAX = MIN * n
    res = search_UglyNumber(MIN, MAX, a, b, c, n)
    # res取余，如果没有余数，说明他就是一个丑数
    la = res % a
    lb = res % b
    lc = res % c
    return res - min(la, lb, lc)

print(N_uglyNumber(2, 3, 5, 3))

'''
Output result：
    6
'''
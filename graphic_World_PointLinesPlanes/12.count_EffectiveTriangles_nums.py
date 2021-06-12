#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
12、计算有效三角形个数
    输入一个列表，列表中是一组非负整数，要求通过编程统计出任取其中3个值做边长可以组成的有效三角形的个数。
注意：列表中可以有重复的值，使用列表中不同位置的数值组成相同的三角形不算重复。例如：
输入[2,2,3,4]，结果将返回3。因为可组成有效三角形的组合如下：
2，3，4（使用第一个2）
2，3，4（使用第二个2）
2，2，3

解题思路：
第一种：采用暴力组合的方式，将所有的组合进行枚举，逐个判断是否满足组成三角形的条件来统计有效三角形的个数；
第二种：采用双指针法，通过指针移动找到符合要求的边长范围。
'''

#暴力枚举的方式
def count_EffectTri_1(nums):
    res = 0
    #从列表中取出3个数值
    for i in range(0, len(nums) - 2):
        a = nums[i]
        for j in range(i+1, len(nums) - 1):
            b = nums[j]
            for k in range(j+1, len(nums)):
                c = nums[k]
                #根据三角形特性判断能否组成三角形
                if a + b > c and a + c > b and b + c > a:
                    res += 1
    return res

print(count_EffectTri_1([2,2,3,4]))
'''
Output result：
    3
'''

def count_EffectTri_2(nums):
    res = 0
    nums.sort() #从小到大排序
    for i in range(0, len(nums) - 2):
        #取出列表中最长边，即：最后一个元素
        c = nums[len(nums) - 1 - i]
        #取最短的边
        p1 = 0
        #取出除最长边c之外的一条最长边
        p2 = len(nums) -1 -i -1
        while p1 < p2:
            #如果满足条件，说明p1-p2之间所有元素都可以作为第三条边
            if nums[p1] + nums[p2] > c:
                res += p2 - p1
                p2 -= 1 #往左移动一位拿到剩下最长的边
            else:
                p1 += 1 #最短边往右移增大
    return res

print(count_EffectTri_2([2,2,3,4]))
'''
Output result：
    3
'''
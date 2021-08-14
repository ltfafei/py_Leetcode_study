#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
14.1、列表两元素之和
    现在输入一个整数列表和一个目标整数，需要从列表中找出两个元素，使其和等于目标元素，结果返回一个列表，包含
所找到的两个元素的下标。如果无法找到这样的两个元素，则返回一个空列表即可。例如：输入列表L为：[1,4,6,8]，输入
目标数12，则需要返回结果[1,3]，因为下标为1的元素4和下标为3的元素8的和为12。
解题方法：
（1）暴力遍历法：循环遍历所有组合进行验证；
（2）双指针法：左右指针夹逼。
'''

#暴力遍历法（两轮循环，时间复杂度O(n)）
def listEleNum_1(l, num):
    #遍历第一个元素
    for i in range(0, len(l)):
        it1 = l[i]
        # 遍历第二个元素
        for j in range(i+1, len(l)):
            it2 = l[j]
            #元素和判断
            if it1 + it2 == num:
                return [i, j]
    return []

print(listEleNum_1([1,4,6,8],12))
'''
Output result：
    [1, 3]
'''

#优化：双指针法
def listEleNum_2(l, num):
    ori = list(l)  #将原列表拷贝一份
    l.sort()  #将列表进行排序
    left = 0  #定义左指针
    right = len(l)-1  #定义右指针
    #两指针重合判断
    while left < right:
        item1 = l[left]
        item2 = l[right]
        res = item1 + item2
        if res > num:
            right -= 1  #左移
        elif res < num:
            left += 1  #右移
        else:
            return [ori.index(item1), ori.index(item2)]
    return []

print(listEleNum_2([1,6,4,8], 12))
'''
Output result：
    [2, 3]
'''

'''
14.2、找出列表中满足条件的三元素组
    现在输入一个整数列表和一个目标整数，找到列表中是否存在三个元素a、b、c，使得a+b+c的和等于输入的
目标整数，并将所有的可能组合返回。例如输入列表为：[1,1,2,4,3,7]，输入的目标整数为6，则需要返回[1,1,4],
[1,2,3]作为答案。
'''

#双指针法
def listEleNum_3(nums, t):
    res = []  #存放结果列表
    nums.sort()  #排序
    #外层遍历，确定第一个元素
    for i in range(0, len(nums)-2):
        #遇到重复元素跳过过滤
        if i > 0 and nums[i] == nums[i-1]:
            continue
        diff = t - nums[i]
        left = i + 1
        right = len(nums) - 1
        #使用双指针法确定剩下的两个元素
        while left < right:
            #进行过滤
            if left > i+1 and nums[left] == nums[left-1]:
                continue
            if right < len(nums)-1 and nums[right] == nums[right+1]:
                continue
            #双指针法核心逻辑
            if nums[left] + nums[right] > diff:
                right -= 1
            elif nums[left] + nums[right] < diff:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
    return res

print(listEleNum_3([1,1,2,4,3,7,6], 6))
'''
Output result：
    [[1, 1, 4], [1, 2, 3]]
'''
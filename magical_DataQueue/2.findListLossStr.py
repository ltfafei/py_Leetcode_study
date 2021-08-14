#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
2、寻找列表中缺失的元素
    输入一个存放数值的列表，列表中的数值都是整数，现在假设列表中的最小值为N，最大值为M，可以确保列表中的元素个数
为（M-N）个，且没有重复的元素，则对于整数闭区间[N, M]来说，到一定缺失了一个数值，要求通过编程将这个缺失的元素找到。
例如：输入列表：[1,2,3,6,4]，则该列表中缺失了5。
'''

class find():
    def findLossStr(self, nums):
        for i in range(min(nums), max(nums)+1):
            if len(nums) == max(nums):
                return ""
            else:
                if i not in nums:
                    return i

run = find()
print(run.findLossStr([1,2,3,6,4]))
'''
Output result：
    5
'''
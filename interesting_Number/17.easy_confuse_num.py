#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
17、易混淆数和中心对称数定义刚好相反。易混淆数是旋转180度之后得到的数字与本身不同。
    现在，输入一个数字，判断其是否是一个易混淆数。
'''

def easy_confuse_Check(num):
    #中心对称数建立映射关系
    dic = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    listNum = list(str(num))
    l = []
    for i in listNum:
        if i not in dic:
            return False    #如果不在dic中，先定义为False
        #每次插入到第一个元素位置，自动逆序
        l.insert(0, dic[i])
        #逆序之后还不相等，说明是易混淆数，返回True
    return l != listNum

print(easy_confuse_Check("101"))
print(easy_confuse_Check("890"))

'''
Output result：
    False
    True
'''
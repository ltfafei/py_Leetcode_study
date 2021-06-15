#!/usr/bin/python
# Env: python3
# Rewrite by afei_0and1

'''
3、字符串全排列
    现在输入一个字符串，要求通过编程将字符串中字符的所有排列组成列表返回。例如：输入“ABC”，可以返回
["ABC"、"ACB"、"BAC"、"BCA"、"CAB"、"CBA"]作为答案。

决策树解题：
    首先需要确定当前决策节点可以选择的分支。对于本题：需要明确每一位可以选择的字符，之后，需要使用回溯
的方法来遍历所有决策节点。即：当第一位选择A之后，下一位可选择的字符有B和C，之后再继续做决策，当决策到
终结点的时候，需要将之前的决策节点进行回溯还原。对于本题，即还原到第一位决策前的状态，继续遍历其他决策
节点。
回溯算法：
    回溯算法在许多编程场景中都有应用。在使用回溯算法时，只需要把握一个原则：如果当前分支可以继续前进就
继续前进；如果到达分支路径的终点或触发了终止条件，就退回来，选择另一个分支继续。
'''

#res：结果列表；index：当前决策字符索引；charList：字符列表
def staringsArrange(res, index, charList):
    #决策到倒数第二位，倒数第一位就已确定
    if index == len(charList) - 1:
        res.append("".join(charList))
    dic = set()
    #遍历进行决策
    for i in range(index, len(charList)):
        item = charList[i]
        if item in dic:
            continue
        dic.add(item)
        temp = charList[index]  #取出当前位字符
        charList[index] = item
        charList[i] = temp
        #递归调用进行决策
        staringsArrange(res, index+1, charList)
        #回溯还原
        charList[index] = temp
        charList[i] = item

def main(string):
    res = []
    staringsArrange(res, 0, list(string))
    return res

print(main("ABC"))
'''
Output result：
    ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']
'''
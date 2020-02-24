'''
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例 1:

输入: 
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入: 
first = "pales"
second = "pal"
输出: False
'''

class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        # 这里直接计算两个字符串的编辑距离，然后进行判断
        len1 = len(first)
        len2 = len(second)
        DP = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        # 初始化
        for i in range(len1+1):
            DP[i][0] = i
        for j in range(len2+1):
            DP[0][j] = j
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if first[i-1] == second[j-1]:
                    DP[i][j] =  DP[i-1][j-1]
                else:
                    DP[i][j]  =  min(DP[i-1][j] + 1,DP[i][j-1] + 1,DP[i-1][j-1]+1)
        if DP[len1][len2] > 1:
            return False
        else:
            return True
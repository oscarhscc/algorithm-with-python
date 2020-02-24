'''
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

 

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #用哈希表
        h = {}
        k = 0
        #统计每个字符出现的次数
        for i in s:
            if i not in h.keys():
                h[i] = 0
            else:
                h[i] += 1
        #每个字符出现的次数为偶数, 或者有且只有一个字符出现的次数为奇数时, 是回文的排列; 否则不是.
        for j in h.values():
            if (j % 2) == 0:
                k += 1
        if k > 1:
            return False
        else:
            return True
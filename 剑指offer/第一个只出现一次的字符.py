'''
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        position = 0
        if len(s) == 0:
            return -1
        for i in s:
            if s.count(i) == 1:
                return position
            else:
                position += 1
        return -1
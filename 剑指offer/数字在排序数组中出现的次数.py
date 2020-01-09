'''
题目描述
统计一个数字在排序数组中出现的次数。
'''
# 解法1
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)

# 解法2
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count = 0
        for j in range(len(data)):
            if data[j] == k:
                count += 1
        return count
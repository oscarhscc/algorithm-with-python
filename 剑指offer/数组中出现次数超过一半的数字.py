'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# 摩尔投票法，最后这个众数的出现次数要大于数组长度的一半

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 1
        res = numbers[0]
        for i in range(1, len(numbers)):
            if count == 0:
                res = numbers[i]
            if res == numbers[i]:
                count += 1
            else:
                count -= 1
        return res if numbers.count(res) > len(numbers)/2 else 0
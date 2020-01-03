'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

# 解法1
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
        	for j in range(len(array[0])):
        		if target == array[i][j]:
        			return True
        return False

# 解法2
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        column = len(array[0])
        i = 0
        j = column - 1
        # 从右上角开始向左下角搜索
        while i < row and j >= 0:
            value = array[i][j]
            if value == target:
                return True
            elif value > target:
                j -= 1
            else:
                i += 1
        return False
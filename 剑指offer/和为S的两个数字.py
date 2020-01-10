'''
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        pre = None
        res = []
        for num in array:
        	# 这种用tsum - num的方法可以少一重循环，提高速度
            if tsum - num in array:
                muti = num * (tsum - num)
                if pre == None or pre > muti:
                	# 记录之前的乘积
                    pre = muti
                    # 记录结果
                    res = [num, tsum - num]
        return sorted(res)
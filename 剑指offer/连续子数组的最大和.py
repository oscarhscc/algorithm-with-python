'''
题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        maxNum = None
        # 当前子串最大和
        tmpNum = 0
        for num in array:
        	# 数组中的第一个数
            if maxNum == None:
                maxNum = num
            # 如果当前子串最大和加上当前数比当前数要小，那么就选择当前的数为当前子串最大和
            if tmpNum + num < num:
                tmpNum = num
            # 如果当前子串最大和加上当前数比当前数要大，那么当前子串最大和等于当前子串最大和加上当前数
            elif tmpNum + num >= num:
                tmpNum += num
            # 进行最大和赋值
            if tmpNum > maxNum:
                maxNum = tmpNum
        return maxNum
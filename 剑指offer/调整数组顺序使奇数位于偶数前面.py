'''
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

# 解法1 常规思路，需要额外的空间
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for i in array:
            if i % 2 == 1:
                odd.append(i)
            if i % 2 == 0:
                even.append(i)
        return odd + even


# 解法2 直接做替换 类似冒泡排序
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        count = 0
        for i in range(0,len(array)):
            for j in range(len(array)-1,i,-1):
                if array[j-1]%2 ==0 and array[j]%2==1:
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array
                    
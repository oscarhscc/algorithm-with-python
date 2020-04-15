'''
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        for i in range(len(height)):
            if height[i] > max1:
                max1 = height[i]
            s1 += max1
        for j in range(len(height) -1, -1, -1):
            if height[j] > max2:
                max2 = height[j]
            s2 += max2
        res = s1 + s2 - max1 * len(height) - sum(height)
        return res
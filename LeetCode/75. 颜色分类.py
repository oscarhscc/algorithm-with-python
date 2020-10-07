'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right, currIdx = 0, len(nums) - 1, 0
        while currIdx <= right:
            if nums[currIdx] == 0:
                nums[left], nums[currIdx] = nums[currIdx], nums[left]
                left += 1
                currIdx += 1
            elif nums[currIdx] == 2:
                nums[right], nums[currIdx] = nums[currIdx], nums[right]
                right -= 1
            else: # 1
                currIdx += 1
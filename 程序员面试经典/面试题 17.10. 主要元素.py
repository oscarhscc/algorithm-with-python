'''
如果数组中多一半的数都是同一个，则称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5
 

示例 2：

输入：[3,2]
输出：-1
 

示例 3：

输入：[2,2,1,1,1,2,2]
输出：2
 

说明：
你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = []
        for num in nums:
            if len(cur) == 0 or cur[-1] == num:
                cur.append(num)
            elif cur[-1] != num:
                cur.remove(cur[-1])
        if len(cur) > 0:
            return cur[-1]
        else:
            return -1
'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_list = {}
        result = []
        # 统计每个数出现的次数
        for i in nums:
            count_list[i] = count_list.get(i, 0) + 1
        # 按照次数从大到小进行排列
        t = sorted(count_list.items(), key=lambda l : l[1], reverse=True)
        # 将前K个数放到结果集中
        for i in range(k):
            result.append(t[i][0])
        return result
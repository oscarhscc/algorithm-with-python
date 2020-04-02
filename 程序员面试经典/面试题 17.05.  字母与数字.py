'''
给定一个放有字符和数字的数组，找到最长的子数组，且包含的字符和数字的个数相同。

返回该子数组，若存在多个最长子数组，返回左端点最小的。若不存在这样的数组，返回一个空数组。

示例 1:

输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]

输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
示例 2:

输入: ["A","A"]

输出: []
提示：

array.length <= 100000
'''

class Solution(object):
    def findLongestSubarray(self, array):
        """
        :type array: List[str]
        :rtype: List[str]
        """
        res, tmp, length, right = {0:0}, 0, 0, 0
        for index, s in enumerate(array):
            tmp += 1 if s.isalpha() else -1
            if tmp not in res:
                res[tmp] = index
            else:
                if tmp == 0:
                    length = index +1
                    right = index+1
                elif index - res[tmp] > length:
                    length = index - res[tmp]
                    right = index +1
        return array[right-length:right]
'''
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

示例：

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出： 3，即数值对(11, 8)
提示：

1 <= a.length, b.length <= 100000
-2147483648 <= a[i], b[i] <= 2147483647
正确结果在区间[-2147483648, 2147483647]内
'''

class Solution(object):
    def smallestDifference(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        a.sort()
        b.sort()
        i = 0
        j = 0
        minimal = 2147483647
        while i < len(a) and j < len(b):
            minimal = min(minimal, abs(a[i] - b[j]))
            if a[i] <= b[j]:
                i += 1
            else:
                j += 1
        return minimal
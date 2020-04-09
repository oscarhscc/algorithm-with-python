'''
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9
'''

class Solution(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        p3, p5, p7 = 0, 0, 0
        dp = [_ for _ in range(k)]
        dp[0] = 1
        for i in range(1, k):
            dp[i] = min(dp[p3] * 3, dp[p5] * 5, dp[p7] * 7)
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
            if dp[i] == dp[p7] * 7:
                p7 += 1
        return dp[-1]
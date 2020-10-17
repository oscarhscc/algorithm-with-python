'''

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。


给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def _DFS(col, xy_dif, xy_sum):
            p = len(col)
            if p == n:
                result.append(col)
                return None
            for q in range(n):
                if q not in col and p-q not in xy_dif and p+q not in xy_sum:
                    _DFS(col + [q], xy_dif + [p-q], xy_sum + [p+q])
        result = []
        _DFS([], [], [])
        return len(result)
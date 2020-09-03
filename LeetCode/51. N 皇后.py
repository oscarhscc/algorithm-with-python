'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 深度优先遍历的辅助函数
        def _DFS(col, xy_dif, xy_sum):
            p = len(col)
            # 搜索终止的条件
            if p == n:
                result.append(col)
                return None
            # 遍历棋盘的列
            for q in range(n):
                if q not in col and p-q not in xy_dif and p+q not in xy_sum:
                    _DFS(col + [q], xy_dif + [p-q], xy_sum + [p+q])
        result = []
        _DFS([], [], [])
        # 双层循环打印输出答案
        return [["." * i + "Q" + "." * (n - i- 1) for i in sol] for sol in result]
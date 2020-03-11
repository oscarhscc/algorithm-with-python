'''
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。

注意：本题相对原题做了扩展

示例:

 输入：4
 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
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
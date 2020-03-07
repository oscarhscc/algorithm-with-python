'''
设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。
设计一种算法，寻找机器人从左上角移动到右下角的路径。


网格中的障碍物和空位置分别用 1 和 0 来表示。

返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
解释: 
输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）
说明：r 和 c 的值均不超过 100。
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m < 1:
            return 0
        n = len(obstacleGrid[0])
        if n < 1:
            return 0
        if 1 == obstacleGrid[0][0]:
            return 0
        dp = [[0]*n for _ in range(m)]  # 外层不能使用*，否则会浅拷贝内层，赋值会带来问题，初始化为０，可以避免额外的赋值
        for i in range(0, m):
            for j in range(0, n):
                if 0 == i and 0 == j:
                    dp[i][j] = 1
                elif 0 == i and 0 != j:
                    if 0 == obstacleGrid[i][j]:
                        dp[i][j] = dp[i][j - 1]
                elif 0 != i and 0 == j:
                    if 0 == obstacleGrid[i][j]:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if 0 == obstacleGrid[i][j]:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
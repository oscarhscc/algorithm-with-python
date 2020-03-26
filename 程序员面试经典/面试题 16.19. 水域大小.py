'''
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

示例：

输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]
提示：

0 < len(land) <= 1000
0 < len(land[i]) <= 1000
'''

class Solution(object):
    def pondSizes(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0:
                    res.append(self.DFS(land, i, j))
        return sorted(res)
    
    def DFS(self, land, i, j):
        m = len(land)
        n = len(land[0])
        count = 0
        if i < 0 or j < 0 or i >= m or j >= n or land[i][j] != 0:
            return 0
        land[i][j] = -1
        count += 1
        count += self.DFS(land, i - 1, j - 1)
        count += self.DFS(land, i - 1, j)
        count += self.DFS(land, i - 1, j + 1)
        count += self.DFS(land, i, j - 1)
        count += self.DFS(land, i, j + 1)
        count += self.DFS(land, i + 1, j)
        count += self.DFS(land, i + 1, j - 1)
        count += self.DFS(land, i + 1, j + 1)
        return count
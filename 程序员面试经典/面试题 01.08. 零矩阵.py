'''
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        x_max = len(matrix)
        y_max = len(matrix[0])
        x_mark = []
        y_mark = []

        for i in range(x_max):
            for j in range(y_max):
                if matrix[i][j] == 0:
                    if i not in x_mark:
                        x_mark.append(i)
                    if j not in y_mark:
                        y_mark.append(j)

        for i_zero_row in x_mark:
            for j_zero_row in range(y_max):
                matrix[i_zero_row][j_zero_row]=0
        for j_zero_col in y_mark:
            for i_zero_col in range(x_max):
                matrix[i_zero_col][j_zero_col]=0
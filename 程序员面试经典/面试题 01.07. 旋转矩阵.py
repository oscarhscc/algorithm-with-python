'''
给定一幅由N × N矩阵表示的图像，其中每个像素的大小为4字节，编写一种方法，将图像旋转90度。

不占用额外内存空间能否做到？

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

# 解法1
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        #若测试用例为 []则n求值会出错, 不过题目没有这个测试用例, 就算有加个判断就好了
        if m > 1 and n > 1:
            matrix[:] = matrix[::-1]                                            #上下翻转
            for i in range(m-1):
                for j in range(n):
                    if i != j and i < j:
                        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]   #沿主对角线翻折


# 解法2
class Solution(object):
	def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # 矩阵的高度
    len1 = len(matrix)
    # 矩阵的宽度
    len2 = len(matrix[0])
    res = []
    childresult = []
    # 倒序遍历高度，取每个元素之首
    for i in range(len2):
        for j in matrix[::-1]:
            childresult.append(j[i])
        res.append(childresult)
        childresult = []
    return res
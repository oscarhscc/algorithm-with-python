'''
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

'''
假设有矩阵：
1	2	3	4
5	6	7	8
9	10	11	12
13	14	15	16
首先matrix.pop(0) = [1,2,3,4]，那么result = [1,2,3,4]
然后剩下的矩阵：
5	6	7	8
9	10	11	12
13	14	15	16
进入turn方法，返回矩阵：
8	12	16
7	11	15
6	10	14
5	9	13
然后matrix.pop(0) = [8,12,16]，那么result = [1,2,3,4,8,12,16]
剩下的矩阵:
7	11	15
6	10	14
5	9	13
进入turn方法，返回矩阵：
15	14	13
11	10	9
7	6	5
然后matrix.pop(0) = [15,14,13]，那么result = [1,2,3,4,8,12,16,15,14,13]
剩下的矩阵：
11	10	9
7	6	5
进入turn方法，返回矩阵：
9	5
10	6
11	7
然后matrix.pop(0) = [9,5]，那么result = [1,2,3,4,8,12,16,15,14,13,9,5]
剩下的矩阵：
10	6
11	7
进入turn方法，返回矩阵：
6	7
10	11
然后matrix.pop(0) = [6,7]，那么result = [1,2,3,4,8,12,16,15,14,13,9,5,6,7]
剩下的矩阵：
10	11
进入turn方法，返回矩阵：
11
10
然后matrix.pop(0) = [11]，那么result = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11]
剩下矩阵：
10
进入turn方法，返回矩阵：
10
然后matrix.pop(0) = [10]，那么result = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

得到 result = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
'''


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result = result + matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result
        
    def turn(self, matrix):
        row = len(matrix)
        coloumn = len(matrix[0])
        B = []
        for i in range(coloumn):
            A = []
            for j in range(row):
                A.append(matrix[j][i])
            B.append(A)
        B.reverse()
        return B

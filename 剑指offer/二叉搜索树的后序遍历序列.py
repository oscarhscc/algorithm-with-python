'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if length == 0:
            return False
        if length == 1:
            return True
        # 后续遍历，根节点一定是序列最后一个
        root = sequence[-1]
        left = 0
        while sequence[left] < root:
                left += 1
        for j in range(left, length-1):
        	# 二叉树根节点右边的节点一定要比根节点大
            if sequence[j] < root:
                return False
        # 递归调用比较根节点的左右子树
        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:length-1])
'''
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

'''
平衡二叉树：左右子树的最大深度差不超过1，先求左右子树的深度，再进行比较
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left = self.depth(pRoot.left)
        right = self.depth(pRoot.right)
        return abs(left - right) <= 1
        
    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return max(left, right) + 1
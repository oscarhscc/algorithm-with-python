'''
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''

'''
要对称，就要左右节点完全一样，左节点的左子树等于右节点的右子树，并且左节点的右子树等于右节点的左子树。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.is_same(pRoot.left, pRoot.right)
        
    def is_same(self, t1, t2):
        if not t1 and not t2:
            return True
        if t1 and t2:
            return t1.val == t2.val and self.is_same(t1.left, t2.right) and self.is_same(t1.right, t2.left)
        return False
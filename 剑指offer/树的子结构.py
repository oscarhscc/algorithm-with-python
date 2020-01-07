'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''



# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 将pRoot1的本身或者左右子树和pRoot2进行比较，看是否有相同的树结构
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
    
    # 判断两棵树是否具有一样的结构，递归比较判断
    def is_subtree(self, A, B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.is_subtree(A.left,B.left) and self.is_subtree(A.right, B.right)
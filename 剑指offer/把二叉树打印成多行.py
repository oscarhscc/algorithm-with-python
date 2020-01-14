'''
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        root = pRoot
        if not root:
            return []
        level = [root]
        result = []
        while level:
            curvalues = []
            nextlevel = []
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if curvalues:
                result.append(curvalues)
            level = nextlevel
        return result
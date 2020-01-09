'''
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        self.Convert(pRootOfTree.left)
        leftTree = pRootOfTree.left
        
        if leftTree:
            while(leftTree.right):
                leftTree = leftTree.right
            pRootOfTree.left,leftTree.right = leftTree,pRootOfTree
            
        self.Convert(pRootOfTree.right)
        rightTree = pRootOfTree.right
        
        if rightTree:
            while(rightTree.left):
                rightTree = rightTree.left
            pRootOfTree.right,rightTree.left = rightTree,pRootOfTree
            
        while(pRootOfTree.left):
            pRootOfTree = pRootOfTree.left
        return pRootOfTree
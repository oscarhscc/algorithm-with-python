'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
'''

'''
根据二叉搜索树的特性，左子树的所有节点值都小于根节点，右子树的所有节点值都大于根节点。
那么我们进行中序遍历，那么得到的序列就是从小到大排列的。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        global result
        result=[]
        self.mid(pRoot)
        if  k <= 0 or len(result) < k:
            return None
        else:
            return result[k-1]
        
    def mid(self, root):
        if not root:
            return [] 
        self.mid(root.left)
        result.append(root)
        self.mid(root.right)
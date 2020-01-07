'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

'''
假如有一颗二叉树：
   8
 6   10
3 7 9 11
从上往下打印的顺序就是：8 6 10 3 7 9 11
1.输出根节点8，并将8的左右节点加入队列[6, 10]
2.将队列中的6输出，并将6的左右节点加入队列中[10, 3, 7]
3.将队列中的10输出，并将10的左右节点加入队列中[3, 7, 9, 11]
4.输出队列中的3，因为3没有左右子树，所以直接输出。
5.同理输出7, 9, 11。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        result = []
        queue = [root]
        if not root:
            return []
        while len(queue):
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
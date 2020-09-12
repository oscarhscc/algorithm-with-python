'''
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        queue = deque([])
        queue.append(root)
        while queue:
            size = len(queue)
            total = 0.0
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(total / size)
        return res
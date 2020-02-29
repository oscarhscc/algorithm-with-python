'''
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:

输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2
示例 2:

输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

输出: null
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        elif root.val > p.val:
            leftRes = self.inorderSuccessor(root.left, p)
            if not leftRes:
                return root
            else:
                return leftRes
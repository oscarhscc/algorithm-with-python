'''
从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。
给定一个由不同节点组成的二叉树，输出所有可能生成此树的数组。

示例:
给定如下二叉树

        2
       / \
      1   3
返回:

[
   [2,1,3],
   [2,3,1]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def BSTSequences(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [[]]
        d = {}
        def f(r):
            if r:
                d[r.val] = []
                r.left and (d[r.val].append(r.left.val) or f(r.left))
                r.right and (d[r.val].append(r.right.val) or f(r.right))
        f(root)
        n = len(d)
        q = [[[root.val], {root.val}]]
        while len(q[0][0]) < n:
            t = []
            for p, c in q:
                for r in p:
                    for v in d[r]:
                        if v not in c:
                            t.append([p + [v], c | {v}])
            q = t
        return [r for r, _ in q]
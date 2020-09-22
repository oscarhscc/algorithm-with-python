'''
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。


示例 1：

输入：[0,0,null,0,0]
输出：1
解释：一台摄像头足以监控所有节点。


示例 2：

输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):  
    def __init__(self):
        self.res = 0
    
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 0：该节点安装了监视器 1：该节点可观，但没有安装监视器 2：该节点不可观
        def dfs(root):
            left = 2
            right = 2
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            if left == 0 or right == 0:
                self.res += 1
                return 1
            elif left == 1 or right == 1:
                return 2
            return 0
        
        if not root:
            return 0
        if dfs(root) == 0:
            self.res += 1
        return self.res
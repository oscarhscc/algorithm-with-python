'''
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        temp=[]
        def inorder(root):
            if root == None:
                return root
            inorder(root.left)
            temp.append(root.val)
            inorder(root.right)
        inorder(root)
        
        dic = collections.Counter(temp)
        max_f = 0
        modes = []
        for key in dic:
            if dic[key] >= max_f:
                max_f = dic[key]
        for key in dic:
            if dic[key] == max_f:
                modes.append(key)
        return modes
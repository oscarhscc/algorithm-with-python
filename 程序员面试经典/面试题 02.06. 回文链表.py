'''
编写一个函数，检查输入的链表是否是回文的。

示例 1：

输入： 1->2
输出： false 
示例 2：

输入： 1->2->2->1
输出： true 
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]
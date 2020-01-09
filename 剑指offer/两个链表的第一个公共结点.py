'''
题目描述
输入两个链表，找出它们的第一个公共结点。
'''

'''
pHead1 A--------
				|_____
				|C	  D     AC + CD + BC = BC + CD + AC
	pHead2 B----
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        node1 = pHead1
        node2 = pHead2
        while node1 is not node2:
            node1 = node1.next if node1 else pHead2
            node2 = node2.next if node2 else pHead1
        return node1
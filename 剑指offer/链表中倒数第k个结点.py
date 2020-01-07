'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        # 遍历链表存入列表中，取第-k个
        while head:
            res.append(head)
            head = head.next
        if k>len(res) or k<1:
            return
        return res[-k]
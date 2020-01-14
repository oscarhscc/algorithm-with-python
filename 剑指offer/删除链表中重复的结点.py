'''
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        d = ListNode(-1)
        d.next = pHead
        pre = d
        cur = pHead
        while cur:
            if cur.next and cur.next.val == cur.val:
                temp = cur.next
                while temp and temp.val == cur.val:
                    temp = temp.next
                pre.next = temp
                cur = temp
            else:
                pre = cur
                cur = cur.next
        return d.next
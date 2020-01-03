'''
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''

# 这里需要注意的是按链表从尾到头返回，所以列表的方法得用insert而不是append。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        head = listNode
        while head:
            result.insert(0, head.val)
            head = head.next
        return result
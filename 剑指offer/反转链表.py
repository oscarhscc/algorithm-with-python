'''
题目描述
输入一个链表，反转链表后，输出新链表的表头。
'''

'''
pre   cur
None   1--->2--->3--->4--->5
      pre  cur
       1--->2--->3--->4--->5
	  pre  cur
       1<---2--->3--->4--->5
           pre  cur
       1<---2--->3--->4--->5
		   pre  cur
       1<---2<---3--->4--->5
              ......
              		      pre  cur
       1<---2<---3<---4<---5
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        cur, pre = pHead, None
        # write code here
        while cur:
            cur.next, pre, cur = pre, cur, cur.next # 改变指针的方向，然后移动指针
        return pre
'''
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

'''
运用快慢双指针，如果两个指针相遇，那么证明链表中存在环。
A-------B-------
	|	|
	C-------
假设有环，在C点相遇。这个时候快指针走的路程为：AB + k * (BC + CB) + BC,
慢指针走的路程为：AB + BC。因为快指针走的路程为慢指针的2倍，所以有：
 AB + k * (BC + CB) + BC = 2 * (AB + BC)
 所以有 AB = k * (BC + CB) - BC  ==> AB = (k-1) * (BC + CB) + CB，
 那么这个时候两个指针分别从C和A出发，速度一样，
 最后相遇的点一定在B点，就可以求出入口节点。
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast = slow = pHead
        hasCycle = False
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                hasCycle = True
                break
        if not hasCycle:
            return None
        
        if hasCycle:
            slow = pHead
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow

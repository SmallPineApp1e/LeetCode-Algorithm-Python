# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/31 21:18
@Desc:
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow, fast = head, head
        while True:
            if fast and fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution2.py
@Time: 2021/5/31 21:03
@Desc: 快慢指针, 快指针比慢指针每次走多1步, 如果有环, 最终一定会与慢指针指向同一节点
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow, fast = head, head.next
        while fast:
            if fast == slow:
                return True
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
        return False
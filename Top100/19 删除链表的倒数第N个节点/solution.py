# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/15 0:03
@Desc:
存储一个虚拟节点dummy，dummy.next = head
快指针fast首先走n步，然后慢指针slow和快指针fast同时向前走，
当fast.next = None时，slow的下一个节点就是要删除的节点，此时slow.next = slow.next.next
"""


class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy
        for i in xrange(0, n, 1):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


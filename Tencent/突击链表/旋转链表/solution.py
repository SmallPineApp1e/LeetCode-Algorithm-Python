# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/31 20:30
@Desc: 核心：快慢指针，找到要旋转的位置，注意k如果大于链表长度，可以取余，效果相同
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head.next is None or k == 0:
            return head
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        k %= length
        if k == 0:
            return head
        curr, fast = head, head
        while k:
            fast = fast.next
            k -= 1
        while fast.next:
            curr = curr.next
            fast = fast.next
        newHead = curr.next
        curr.next = None
        fast.next = head
        return newHead
# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 23:19
@Desc:
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        pre, curr, next = None, head, head.next
        while next is not None:
            curr.next = pre
            pre = curr
            curr = next
            next = curr.next
        curr.next = pre
        return curr


if __name__ == '__main__':
    s = Solution()
    l5 = ListNode(5)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    s.reverseList(l1)
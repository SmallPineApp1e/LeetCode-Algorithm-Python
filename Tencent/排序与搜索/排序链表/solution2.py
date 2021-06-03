# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution2.py
@Time: 2021/6/1 16:11
@Desc: 分治法，分的过程是O(N*logN)，治的过程是O(N)，总的时间复杂度就是O(NlogN)，而且在治的过程中就是“对两个有序链表进行合并”
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        if head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head1, head2 = head, slow.next
        slow.next = None
        left, right = self.sortList(head1), self.sortList(head2)
        newHead = self.mergeTwoLists(left, right)
        return newHead

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        newCurr, curr1, curr2 = dummy, l1, l2
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                newCurr.next = curr1
                curr1 = curr1.next
            else:
                newCurr.next = curr2
                curr2 = curr2.next
            # print "%i " % newCurr.val,
            newCurr = newCurr.next
        if curr1 is not None:
            newCurr.next = curr1
        elif curr2 is not None:
            newCurr.next = curr2
        # print "%i " % newCurr.val,
        return dummy.next


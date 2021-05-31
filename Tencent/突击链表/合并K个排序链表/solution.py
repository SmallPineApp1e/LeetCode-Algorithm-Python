# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/31 19:40
@Desc:
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) != 1:
            l1, l2 = lists.pop(0), lists.pop(0)
            newList = self.mergeTwoLists(l1, l2)
            lists.append(newList)
        return lists.pop(0)

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
            print "%i " % newCurr.val,
            newCurr = newCurr.next
        if curr1 is not None:
            newCurr.next = curr1
        elif curr2 is not None:
            newCurr.next = curr2
        print "%i " % newCurr.val,
        return dummy.next
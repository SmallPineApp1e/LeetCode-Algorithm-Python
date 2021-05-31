# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/31 19:25
@Desc:
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
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


if __name__ == '__main__':
    s = Solution()
    l1_1 = ListNode(4)
    l1_2 = ListNode(2, l1_1)
    l1_3 = ListNode(1, l1_2)
    l2_1 = ListNode(4)
    l2_2 = ListNode(3, l2_1)
    l2_3 = ListNode(1, l2_2)
    s.mergeTwoLists(l1_3, l2_3)






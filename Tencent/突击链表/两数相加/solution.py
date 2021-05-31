# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/31 19:09
@Desc:
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy, curr1, curr2 = ListNode(-1), l1, l2
        carry, newCurr = 0, dummy
        while curr1 is not None and curr2 is not None:
            s = curr1.val + curr2.val + carry
            newCurr.next = ListNode(s % 10)
            carry = s // 10
            curr1 = curr1.next
            curr2 = curr2.next
            newCurr = newCurr.next
        while curr1 is not None:
            s = carry + curr1.val
            newCurr.next = ListNode(s % 10)
            carry = s // 10
            curr1 = curr1.next
            newCurr = newCurr.next
        while curr2 is not None:
            s = carry + curr2.val
            newCurr.next = ListNode(s % 10)
            carry = s // 10
            curr2 = curr2.next
            newCurr = newCurr.next
        if carry == 1:
            newCurr.next = ListNode(carry)
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    l1_1 = ListNode(3)
    l1_2 = ListNode(4, l1_1)
    l1_3 = ListNode(2, l1_2)
    l2_1 = ListNode(4)
    l2_2 = ListNode(6, l2_1)
    l2_3 = ListNode(5, l2_2)

    print s.addTwoNumbers(l1_3, l2_3)
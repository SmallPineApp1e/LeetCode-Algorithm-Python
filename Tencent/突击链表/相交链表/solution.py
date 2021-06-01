# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/1 10:24
@Desc: 采用list存储已遍历的节点, 两条指针各自遍历一次, 如果在遍历过程中发现节点已存在list中, 证明它是相交的起始节点(超时)
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l = []
        curr1, curr2 = headA, headB
        while curr1:
            l.append(curr1)
            curr1 = curr1.next
        while curr2:
            if curr2 in l:
                return curr2
            curr2 = curr2.next
        return None
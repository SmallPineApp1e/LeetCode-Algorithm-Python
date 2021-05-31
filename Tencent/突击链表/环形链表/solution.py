# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/31 20:58
@Desc: O(N)额外空间复杂度, 用list保存已遍历的节点, 如果遍历过程发现在list中已存在, 则说明有环
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
        l, curr = [], head
        while True:
            if curr is None:
                return True
            elif curr in l:
                return True
            else:
                l.append(curr)
            curr = curr.next
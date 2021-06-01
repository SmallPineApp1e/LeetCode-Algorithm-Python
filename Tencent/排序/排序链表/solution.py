# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/1 15:47
@Desc: 建立小根堆进行排序, 建立小根堆的过程是O(NlogN)，取出元素的过程是O(logN)，综合就是O(NlogN)
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        import heapq
        heap, dummy = [], ListNode(-1)
        curr = dummy
        while head:
            heapq.heappush(heap, head.val)
            head = head.next
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        return dummy

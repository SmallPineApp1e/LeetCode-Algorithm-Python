# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution2.py
@Time: 2021/5/31 19:54
@Desc: 对K个链表的当前元素建立小根堆，使用O(logK)的时间选出最小元素，总时间复杂度优化成O(N*logK)
"""


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
        import heapq
        heap, dummy = [], ListNode(-1)
        curr = dummy
        for i in xrange(0, len(lists), 1):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
            curr = curr.next
        return dummy.next

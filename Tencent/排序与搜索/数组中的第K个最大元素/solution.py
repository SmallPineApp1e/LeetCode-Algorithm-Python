# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/3 19:24
@Desc:
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []
        for idx, num in enumerate(nums):
            heapq.heappush(heap, num * -1)
        res = 0
        while heap and k > 0:
            res = heapq.heappop(heap) * -1
            k -= 1
        return res
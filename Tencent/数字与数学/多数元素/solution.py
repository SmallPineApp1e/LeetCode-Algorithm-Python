# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/1 15:03
@Desc: 将整个数组排序，在中间部分的数字一定是众数，因为众数至少是出现了 n/2 次
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums) / 2]

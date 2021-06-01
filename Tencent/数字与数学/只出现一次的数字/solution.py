# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/1 14:58
@Desc: 两个相同的数字异或等于0，所以整个数组元素两两异或后，最后剩下的一定是只出现一次的数字
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(0, len(nums), 1):
            res ^= nums[i]
        return res
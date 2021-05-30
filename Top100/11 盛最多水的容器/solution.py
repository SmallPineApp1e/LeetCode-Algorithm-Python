# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/4/29 21:29
@Desc: 双指针的应用，每一轮计算储水量后将较短高度的指针向中间移动一位
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 1:
            return 0

        maxWater, lo, hi = 0, 0, length - 1
        while lo < hi:
            maxWater = max(min(height[lo], height[hi]) * (hi - lo), maxWater)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1

        return maxWater


if __name__ == '__main__':
    s = Solution()
    s.maxArea([2,3,4,5,18,17,6])
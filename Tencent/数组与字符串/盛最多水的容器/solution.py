# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 9:44
@Desc:
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            res = max(res, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print s.maxArea([1, 1])
    print s.maxArea([4, 3, 2, 1, 4])
    print s.maxArea([1, 2, 1])

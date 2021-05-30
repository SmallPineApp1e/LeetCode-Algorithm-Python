# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 11:22
@Desc:
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for idx, nums in enumerate(nums):
            if nums in d:
                return True
            d[nums] = idx
        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsDuplicate([1, 2, 3, 1])
    print s.containsDuplicate([1, 2, 3, 4])
    print s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/13 22:20
@Desc:
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(subset, idx):
            res.append(subset)
            for i in xrange(idx, len(nums)):
                dfs(subset + [nums[i]], i + 1)
        res = []
        dfs([], 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.subsets([1, 2, 3])
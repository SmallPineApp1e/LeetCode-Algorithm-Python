# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution2.py
@Time: 2021/6/12 18:28
@Desc:
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(i, subset):
            res.append(subset)
            for j in xrange(i, length):
                dfs(j + 1, subset + [nums[j]])

        res, length = [], len(nums)
        dfs(0, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print s.subsets([1, 2, 3])

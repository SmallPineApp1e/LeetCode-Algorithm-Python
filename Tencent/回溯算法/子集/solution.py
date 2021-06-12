# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/11 10:38
@Desc:
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 1:
            return [[]]
        res, maxElement = [[]], length
        for i in xrange(1, maxElement + 1):
            self.dfs(i, 0, i, [], res, nums, length)
        return res

    def dfs(self, ele_cnt, idx, curr_cnt, curr_list, res, nums, length):
        if curr_cnt <= 0:
            newSubset = curr_list[:]
            res.append(newSubset)
            return
        for i in xrange(idx, length):
            curr_list.append(nums[i])
            self.dfs(ele_cnt, i + 1, curr_cnt - 1, curr_list, res, nums, length)
            curr_list.remove(nums[i])


if __name__ == '__main__':
    s = Solution()
    print s.subsets([1, 2, 3])

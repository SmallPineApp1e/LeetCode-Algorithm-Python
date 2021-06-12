# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/12 18:36
@Desc:
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(curr_pos):
            if curr_pos == length:
                res.append(temp[:])
                return
            for i in xrange(0, length):
                if not isUsed[i]:
                    isUsed[i] = True
                    temp[curr_pos] = nums[i]
                    dfs(curr_pos + 1)
                    isUsed[i] = False

        res, length = [], len(nums)
        temp, isUsed = [0] * length, [False] * length
        dfs(0)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.permute([1, 2, 3])
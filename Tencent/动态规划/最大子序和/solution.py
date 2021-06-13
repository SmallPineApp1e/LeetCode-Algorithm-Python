# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/13 17:40
@Desc:  贪心算法，在遍历过程中比较sum是否大于0，如果是说明sum对下一个结果有增益效果，可以继续累加，
        否则没有增益效果（不加反减），直接将sum设置为下一个元素
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum, res = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            if sum > 0:
                sum += nums[i]
            else:
                sum = nums[i]
            res = max(res, sum)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 10:46
@Desc:
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length, k = len(nums), 1
        res = [1] * length
        for i in xrange(0, length, 1):
            res[i] = k
            k *= nums[i]
        k = 1
        for i in xrange(length - 1, -1, -1):
            res[i] *= k
            k *= nums[i]
        return res


if __name__ == '__main__':
    s = Solution()
    print s.productExceptSelf([1,2,3,4])
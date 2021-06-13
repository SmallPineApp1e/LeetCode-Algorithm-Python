# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution2.py
@Time: 2021/6/13 17:53
@Desc:  动态规划法，dp[i]代表以nums[i]为结尾的最大子序和，
        状态转移方程：dp[i+1] = max(dp[i] + nums[i+1], nums[i+1])，代表下一个最大子序和可能是当前子序和加下一个元素，或者是从下一个元素为新
                    的起始元素作为最大子序和
"""


class Solution(object):
    def maxSubArray(self, nums):
        dp, maxSum = [0] * len(nums), nums[0]
        dp[0] = nums[0]
        for i in xrange(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            maxSum = max(maxSum, dp[i])
        return maxSum
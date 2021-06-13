# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/13 21:56
@Desc:
"""


class Solution(object):
    # 解法1（模拟）：每天都买入，在第二天售出，然后在第二天再买入，以此类推
    # 注意如果前一天的股票数值比后一天大，那么是亏损的（没有盈利），此时应该返回0
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price, result = prices[0], 0
        for i in xrange(1, len(prices)):
            result += max(prices[i] - price, 0)
            price = prices[i]
        return result

    # 解法2（动态规划）：dp[i] 代表第i天能够获得的总利润值
    # dp[i + 1] = dp[i] + max(0, nums[i + 1] - nums[i])
    def maxProfit2(self, prices):
        dp = [0] * len(prices)
        for i in xrange(0, len(dp) - 1):
            dp[i + 1] = dp[i] + max(0, prices[i + 1] - prices[i])
        return dp[len(dp) - 1]


if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([7, 1, 5, 3, 6, 4])
    print s.maxProfit([1, 2, 3, 4, 5])
    print s.maxProfit([7, 6, 4, 3, 1])
    print s.maxProfit2([7, 1, 5, 3, 6, 4])
    print s.maxProfit2([1, 2, 3, 4, 5])
    print s.maxProfit2([7, 6, 4, 3, 1])

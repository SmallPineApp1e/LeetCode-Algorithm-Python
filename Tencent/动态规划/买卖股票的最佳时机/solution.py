# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/13 18:07
@Desc:
"""


class Solution(object):
    # 解法1（超时）：暴力枚举每一天买入后可以获取到的最大利润
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(0, len(prices)):
            for j in xrange(i + 1, len(prices)):
                temp = 0
                if prices[j] > prices[i]:
                    temp = prices[j] - prices[i]
                res = max(res, temp)
        return res

    # 解法2：设dp[i][0]是第i天没有持有股票的最大收益，dp[i][1]是第i天持有股票时的最大收益
    #       dp[i][0] = max(prices[i] - dp[i - 1][1], dp[i - 1][0])
    #       dp[i][1] = max(-price[i], dp[i - 1][1])
    def maxProfit2(self, prices):
        dp = [[0, 0]] * len(prices)
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in xrange(1, len(dp)):
            dp[i][0] = max(prices[i] + dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = max(-prices[i], dp[i - 1][1])
        return dp[len(dp) - 1][0]

    # 解法3：维护最小值，判断当前元素与最小值之间的差值，取差值的最大值就可以计算出最大利润
    def maxProfit3(self, prices):
        minPrice, maxProfit = prices[0], 0
        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit


if __name__ == '__main__':
    s = Solution()
    print s.maxProfit2([7, 1, 5, 3, 6, 4])
    print s.maxProfit2([2, 4, 1])
    print s.maxProfit2([7, 6, 4, 3, 1])
    print s.maxProfit3([7, 1, 5, 3, 6, 4])
    print s.maxProfit3([2, 4, 1])
    print s.maxProfit3([7, 6, 4, 3, 1])

# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/13 22:12
@Desc:
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        # base state
        for j in xrange(0, n):
            dp[j] = 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    print s.uniquePaths(3, 7)

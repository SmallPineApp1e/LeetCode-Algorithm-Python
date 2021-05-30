# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 15:02
@Desc:
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num, res = 1, []
        for i in xrange(0, n, 1):
            res.append([0] * n)
        t, b, l, r = 0, len(res) - 1, 0, len(res[0]) - 1
        while num <= n ** 2:
            # 右
            for i in xrange(l, r + 1, 1):
                res[t][i] = num
                num += 1
                i += 1
            t += 1
            # 下
            for i in xrange(t, b + 1, 1):
                res[i][r] = num
                num += 1
            r -= 1
            # 左
            for i in xrange(r, l - 1, -1):
                res[b][i] = num
                num += 1
            b -= 1
            # 上
            for i in xrange(b, t - 1, -1):
                res[i][l] = num
                num += 1
            l += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.generateMatrix(3)

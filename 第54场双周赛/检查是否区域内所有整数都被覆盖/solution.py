# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/12 22:30
@Desc:
"""


class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        res = True
        for i in xrange(left, right + 1):
            temp = False
            for j, ran in enumerate(ranges):
                if ran[0] <= i <= ran[1]:
                    temp = True
                    break
            res &= temp
        return res


if __name__ == '__main__':
    s = Solution()
    print s.isCovered([[1, 2], [3, 4], [5, 6]], 2, 5)
    print s.isCovered([[1, 10], [10, 20]], 21, 21)
    print s.isCovered([[1, 1]], 1, 50)

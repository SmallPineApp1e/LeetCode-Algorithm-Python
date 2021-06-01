# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/1 15:36
@Desc:
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n & (n - 1)) == 0 and n != 0


if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfTwo(1)
    print s.isPowerOfTwo(2)
    print s.isPowerOfTwo(0)
    print s.isPowerOfTwo(10)
    print s.isPowerOfTwo(8)
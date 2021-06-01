# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/1 11:08
@Desc:
"""
import sys


class Solution(object):
    def reverse(self, x):
        MAX_INT = 2 ** 31 - 1
        """
        :type x: int
        :rtype: int
        """
        flag = -1 if x < 0 else 1
        x = -x if x < 0 else x
        reverse = 0
        while x:
            num = x % 10
            reverse = reverse * 10 + num
            if reverse > MAX_INT or (reverse == MAX_INT / 10 and num > MAX_INT % 10):
                return 0
            x /= 10
        return reverse * flag


if __name__ == '__main__':
    s = Solution()
    print s.reverse(123)
    print s.reverse(-123)
    print s.reverse(0)
    print s.reverse(1230)
    print s.reverse(120)
    print s.reverse(10)
    print s.reverse(1534236469)
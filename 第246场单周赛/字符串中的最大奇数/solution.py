# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/20 12:49
@Desc:
"""


class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in xrange(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""
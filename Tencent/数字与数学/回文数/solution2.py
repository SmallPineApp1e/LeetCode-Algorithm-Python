# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution2.py
@Time: 2021/6/1 14:53
@Desc: 回文数一定是正序=倒序，所以不用转换为字符串，直接将数字反转，看看是否等于原来的数字即可
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reverse, temp = 0, x
        while temp:
            reverse = reverse * 10 + temp % 10
            temp /= 10
        return reverse == x
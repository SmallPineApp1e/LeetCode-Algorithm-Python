# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/1 11:18
@Desc:
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        length = len(s)
        for i in xrange(0, length // 2, 1):
            if s[i] != s[length - i - 1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(121)
    print s.isPalindrome(-121)
    print s.isPalindrome(10)
    print s.isPalindrome(-10)
    print s.isPalindrome(0)
# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 10:30
@Desc:
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([''.join(reversed(e)) for e in s.split(" ")])


if __name__ == '__main__':
    s = Solution()
    print s.reverseWords("Let's take LeetCode contest")
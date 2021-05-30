# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/4/29 21:44
@Desc: 中心扩展法，每个字母有两种做法：以自身为中心扩展（奇数长度的回文串）和与后面的字母组成一对字母（偶数长度的回文串）
"""


class Solution(object):
    def longestPalindrome(self, s):
        res, length, i, end = "", len(s), 0, len(s) - 1
        for i in xrange(0, length, 1):
            res = s[i:i + 1] if len(res) < 2 else res
            # 以自身为中心扩展(奇数回文串)
            left, right = i - 1, i + 1
            while left >= 0 and right <= end and s[left] == s[right]:
                res = s[left:right+1] if len(res) < right - left + 1 else res
                left -= 1
                right += 1
            # 以s[i]和s[i+1]为中心扩展(偶数回文串)
            if i < length - 1 and s[i] == s[i + 1]:
                res = s[i:i + 2] if len(res) < 3 else res
                left, right = i - 1, i + 2
                while left >= 0 and right <= end and s[left] == s[right]:
                    res = s[left:right + 1] if len(res) < right - left + 1 else res
                    left -= 1
                    right += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome("cccc")
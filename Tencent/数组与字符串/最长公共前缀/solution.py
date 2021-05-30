# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/29 22:56
@Desc:
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        if len(strs) < 1:
            return res
        for i in xrange(0, len(strs[0]), 1):
            character = strs[0][i]
            for idx, s in enumerate(strs):
                if i >= len(s) or character != s[i]:
                    return res
            res += character
        return res


if __name__ == "__main__":
    s = Solution()
    print s.longestCommonPrefix(["flower", "flow", "flight"])
    print s.longestCommonPrefix(["dog", "racecar", "car"])

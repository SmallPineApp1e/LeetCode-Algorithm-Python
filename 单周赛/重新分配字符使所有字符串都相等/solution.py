# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/13 10:32
@Desc:
"""


class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        m, length = {}, len(words)
        for idx, word in enumerate(words):
            for i in xrange(0, len(word)):
                m[word[i]] = 1 if word[i] not in m else m[word[i]] + 1
        for k, v in m.items():
            if v % length != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.makeEqual(["abc", "aabc", "bc"])
    print s.makeEqual(["ab", "a"])
    print s.makeEqual(["a", "a"])
    print s.makeEqual(["a", "b"])

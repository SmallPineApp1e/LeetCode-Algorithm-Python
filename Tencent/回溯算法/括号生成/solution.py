# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/11 10:24
@Desc:
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs("", 0, 0, 2 * n, res)
        return res

    def dfs(self, s, left, right, n, res):
        if left + right == n:
            res.append(s)
            return
        if left < n / 2:
            self.dfs(s + "(", left + 1, right, n, res)
        if left > right:
            self.dfs(s + ")", left, right + 1, n, res)


if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)

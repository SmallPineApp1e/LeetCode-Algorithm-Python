# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/12 23:37
@Desc: 精选题解：https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res, head = [0], 1
        for i in xrange(0, n):
            for j in xrange(len(res) - 1, -1, -1):
                res.append(res[j] + head)
            head <<= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.grayCode(3)

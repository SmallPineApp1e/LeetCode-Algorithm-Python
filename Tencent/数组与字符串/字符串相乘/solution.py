# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 10:00
@Desc:
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for idx2 in xrange(len(num2) - 1, -1, -1):
            for idx1 in xrange(len(num1) - 1, -1, -1):
                n1, n2 = int(num1[idx1]), int(num2[idx2])
                mul = n1 * n2
                res[idx1 + idx2 + 1] += mul
                res[idx1 + idx2] += res[idx1 + idx2 + 1] / 10
                res[idx1 + idx2 + 1] %= 10
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        return ''.join([str(ele) for ele in res[start:]])


if __name__ == '__main__':
    s = Solution()
    print s.multiply("123", "456")
    print s.multiply("2", "3")
    print s.multiply("123456789", "987654321")

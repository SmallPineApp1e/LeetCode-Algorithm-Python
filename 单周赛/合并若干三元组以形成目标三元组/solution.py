# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/13 11:19
@Desc:
"""


class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        res = [0] * 3
        for ele in triplets:
            if ele[0] > target[0] or ele[1] > target[1] or ele[2] > target[2]:
                continue
            res[0] = max(res[0], ele[0])
            res[1] = max(res[1], ele[1])
            res[2] = max(res[2], ele[2])
        return res[0] == target[0] and res[1] == target[1] and res[2] == target[2]


if __name__ == '__main__':
    s = Solution()
    print s.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5])
    print s.mergeTriplets([[1, 3, 4], [2, 5, 8]], [2, 5, 8])
    print s.mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5])
    print s.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5])
    print s.mergeTriplets([[1, 3, 1]], [1, 3, 1])

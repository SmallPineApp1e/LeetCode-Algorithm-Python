# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/12 22:39
@Desc:
"""


class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        for idx, num in enumerate(chalk):
            sum += num
        k %= sum
        if k == 0:
            return 0
        for idx, num in enumerate(chalk):
            if k < num:
                return idx
            else:
                k -= num
        return -1


if __name__ == '__main__':
    s = Solution()
    print s.chalkReplacer([5, 1, 5], 22)
    print s.chalkReplacer([3, 4, 1, 2], 25)

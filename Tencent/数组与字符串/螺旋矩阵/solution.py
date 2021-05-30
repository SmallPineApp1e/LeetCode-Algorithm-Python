# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 11:26
@Desc:
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while True:
            # 右
            i = l
            while i <= r:
                res.append(matrix[t][i])
                i += 1
            t += 1
            if t > b:
                break
            # 下
            i = t
            while i <= b:
                res.append(matrix[i][r])
                i += 1
            r -= 1
            if l > r:
                break
            # 左
            i = r
            while i >= l:
                res.append(matrix[b][i])
                i -= 1
            b -= 1
            if t > b:
                break
            # 上
            i = b
            while i >= t:
                res.append(matrix[i][l])
                i -= 1
            l += 1
            if l > r:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

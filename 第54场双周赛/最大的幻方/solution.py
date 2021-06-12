# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/12 22:43
@Desc:
"""


class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col, maxSize = len(grid), len(grid[0]), 1
        dp = [[1] * col] * row
        for i in xrange(0, row):
            for j in xrange(0, col):
                dp[i][j] = 1
        for i in xrange(0, row):
            for j in xrange(0, col):
                for k in xrange(2, min(row, col) + 1):
                    check = self.checkIsMagicSquare(grid, i, j, row, col, k)
                    if check:
                        dp[i][j] = k
                        maxSize = max(maxSize, dp[i][j])
        return maxSize

    def checkIsMagicSquare(self, grid, curr_row, curr_col, max_row, max_col, size):
        if curr_col + size - 1 >= max_col or curr_row + size - 1 >= max_row:
            return False
        sum, tempSum = 0, 0
        # 求每一行的和
        for i in xrange(curr_row, curr_row + size):
            for j in xrange(curr_col, curr_col + size):
                tempSum += grid[i][j]
            if sum == 0:
                sum = tempSum
                tempSum = 0
                continue
            elif sum != tempSum:
                return False
            tempSum = 0
        # 求每一列的和
        for j in xrange(curr_col, curr_col + size):
            for i in xrange(curr_row, curr_row + size):
                tempSum += grid[i][j]
            if sum == 0:
                sum = tempSum
                continue
            elif sum != tempSum:
                return False
            tempSum = 0
        # 求对角线的和
        for i in xrange(1, size + 1):
            tempSum += grid[curr_row + i - 1][curr_col + i - 1]
        if sum != tempSum:
            return False
        tempSum = 0

        for i in xrange(1, size + 1):
            tempSum += grid[curr_row + i - 1][curr_col + size - i]
        if sum != tempSum:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.largestMagicSquare([[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]])
    print s.largestMagicSquare([[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]])

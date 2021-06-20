# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/20 12:54
@Desc:
"""


class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        row = len(grid2)
        col = len(grid2[0])
        visit = []
        for i in xrange(0, row, 1):
            visit.append([False] * col)
        res, idxs = 0, []
        for i in xrange(0, row, 1):
            for j in xrange(0, col, 1):
                if not visit[i][j] and grid2[i][j] == 1:
                    idx = []
                    self.dfs(grid2, i, j, row, col, visit, idx)
                    idxs.append(idx)
        # print idxs
        for i in xrange(0, len(idxs), 1):
            flag = True
            for j in xrange(0, len(idxs[i]), 1):
                if grid2[idxs[i][j][0]][idxs[i][j][1]] == 1 and grid1[idxs[i][j][0]][idxs[i][j][1]] == 0:
                    flag = False
                    break
            if flag:
                res += 1
        return res

    def dfs(self, grid2, i, j, row, col, visit, idx):
        if i < 0 or j < 0 or i >= row or j >= col or visit[i][j] or grid2[i][j] != 1:
            return
        visit[i][j] = True
        idx.append([i, j])
        self.dfs(grid2, i + 1, j, row, col, visit, idx)
        self.dfs(grid2, i, j + 1, row, col, visit, idx)
        self.dfs(grid2, i - 1, j, row, col, visit, idx)
        self.dfs(grid2, i, j - 1, row, col, visit, idx)
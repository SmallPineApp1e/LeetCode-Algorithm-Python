# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/3 20:57
@Desc:
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.res = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0
        leftSum = self.dfs(root.left)
        rightSum = self.dfs(root.right)
        self.res = max(leftSum + rightSum + root.val, self.res)
        outputMaxSum = max(leftSum, rightSum) + root.val
        return outputMaxSum if outputMaxSum > 0 else 0
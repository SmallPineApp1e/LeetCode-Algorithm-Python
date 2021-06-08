# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/8 10:59
@Desc:
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.LEFT = 0
        self.RIGHT = 1
        self.BOTH_SIDE = 2

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        side = self.checkSide(root, p, q)
        if side == self.BOTH_SIDE:
            return root
        else:
            if root == p or root == q:
                return root
            if side == self.LEFT:
                return self.lowestCommonAncestor(root.left, p, q)
            elif side == self.RIGHT:
                return self.lowestCommonAncestor(root.right, p, q)

    def checkSide(self, root, p, q):
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return self.BOTH_SIDE
        elif p.val < root.val and q.val < root.val:
            return self.LEFT
        else:
            return self.RIGHT

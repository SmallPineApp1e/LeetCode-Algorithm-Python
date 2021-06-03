# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/3 20:20
@Desc:
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.cnt = 0
        self.res = None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt = k
        self.inorder(root)
        return self.res.val

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.cnt -= 1
        if self.cnt == 0:
            self.res = root
            return
        self.inorder(root.right)
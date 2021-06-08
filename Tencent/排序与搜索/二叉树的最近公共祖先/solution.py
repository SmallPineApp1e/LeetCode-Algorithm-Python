# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/8 11:36
@Desc: 暴力解法，以根节点开始，判断p和q存在于（两侧）还是（左侧）还是（右侧），总共通过29/31个样例，证明思想是对的
        但时间复杂度太高了，O(N*logN)
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        left1 = self.findElement(root.left, p)
        left2 = self.findElement(root.left, q)
        right1 = self.findElement(root.right, p)
        right2 = self.findElement(root.right, q)
        # 两侧
        if (left1 and right2) or (left2 and right1):
            return root
        # 一侧
        if left1 and left2:
            if root == left1 or root == left2:
                return root
            return self.lowestCommonAncestor(root.left, p, q)
        if right1 and right2:
            if root == right1 or root == right2:
                return root
            return self.lowestCommonAncestor(root.right, p, q)

    def findElement(self, root, target):
        if not root:
            return None
        if root == target:
            return root
        left = self.findElement(root.left, target)
        right = self.findElement(root.right, target)
        return left if left is not None else right
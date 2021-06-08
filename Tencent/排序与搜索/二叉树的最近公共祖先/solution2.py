# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution2.py
@Time: 2021/6/8 12:42
@Desc:  如果先找到某个节点p/q，那证明p/q就是这棵树的最近公共祖先，直接返回，然后每一层返回时
        判断左子树的最近公共祖先和右子树的公共祖先，如果都不是空，说明p和q分布在左子树和右子树，返回root
        如果左子树的最近公共祖先为空，证明p和q都在右子树上，返回right
        如果右子树的最近公共祖先为空，证明p和q都在左子树上，返回left
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
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        else:
            return right
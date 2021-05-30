# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/17 23:05
@Desc: 利用栈，遇到"("或"["或"{“时，压入")"或"]"或"}"，遇到右括号时，匹配栈顶元素，如果不相等则说明不是有效括号
"""


class Solution(object):
    def isValid(self, s):
        stack = []
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(")")
            elif ch == "[":
                stack.append("]")
            elif ch == "{":
                stack.append("}")
            else:
                if len(stack) < 1 or stack.pop(-1) != ch:
                    return False
        return True if len(stack) == 0 else False
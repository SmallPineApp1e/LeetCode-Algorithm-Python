# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 9:26
@Desc:
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, res = [], True
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(")")
            elif ch == "[":
                stack.append("]")
            elif ch == "{":
                stack.append("}")
            else:
                if len(stack) < 1 or stack.pop(len(stack) - 1) != ch:
                    res = False
                    break
        if len(stack) > 0:
            res = False
        return res


if __name__ == '__main__':
    s = Solution()
    print s.isValid("()")
    print s.isValid("()[]{}")
    print s.isValid("(]")
    print s.isValid("([)]")
    print s.isValid("{[]}")
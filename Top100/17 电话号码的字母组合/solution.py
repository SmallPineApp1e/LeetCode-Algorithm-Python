# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/8 23:05
@Desc:
"""


class Solution(object):
    def letterCombinations(self, digits):
        m = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        res = []
        digitsLength = len(digits)
        if digitsLength < 1:
            return res
        self.dfs(digits, 0, digitsLength, "", res, m)
        return res

    def dfs(self, digits, begin, end, combination, res, m):
        if begin == end:
            res.append(combination)
            return
        characters = m[digits[begin]]
        for idx, ch in enumerate(characters):
            temp = combination + ch
            self.dfs(digits, begin + 1, end, temp, res, m)


if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations("23")
    print s.letterCombinations("")
    print s.letterCombinations("2")
    print s.letterCombinations("234")
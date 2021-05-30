# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/29 20:26
@Desc:
"""


class Solution(object):
    def myAtoi(self, s):
        INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31
        s = self.strip(s)
        if s == '':
            return 0
        res, flag, start = 0, 1, 0
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                flag = -1
            start += 1
        for i in range(start, len(s), 1):
            if ord(s[i]) - ord('0') >= 10 or ord(s[i]) - ord('0') < 0:
                return res * flag
            num = int(s[i])
            res = res * 10 + num
            if res > INT_MAX or (res == (INT_MAX / 10) and num > INT_MAX % 10):
                if flag < 0:
                    return INT_MIN
                else:
                    return INT_MAX
        return res * flag

    def strip(self, s):
        # 去除前导空格
        for i in range(0, len(s), 1):
            if s[i] == ' ':
                continue
            return s[i:]
        return ''


if __name__ == '__main__':
    s = Solution()
    print s.myAtoi("42")
    print s.myAtoi("   -42")
    print s.myAtoi("4193 with words")
    print s.myAtoi("words and 987")
    print s.myAtoi("-91283472332")
    print s.myAtoi("3.14")
    print s.myAtoi("21474836460")
    print s.myAtoi("-2147483648")
    print s.myAtoi("-2147483649")
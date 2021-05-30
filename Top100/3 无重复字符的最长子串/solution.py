# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/1 23:50
@Desc: 用map记录所有字符第一次出现的下标i，如果某个字符出现在map中，将遍历的下标left = max(left, characterFirstPosMap[s[right]] + 1)
        要比较left本身取最大的原因在于有可能left已经在该出现过的字符的右边了，这种情况之前已经被考虑在内了，所以可以排除
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        characterFirstPosMap, res = {}, 0
        left, right, length = 0, 0, len(s)
        while right < length:
            if s[right] in characterFirstPosMap:
                left = max(left, characterFirstPosMap[s[right]] + 1)
            characterFirstPosMap[s[right]] = right
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("dvdf")
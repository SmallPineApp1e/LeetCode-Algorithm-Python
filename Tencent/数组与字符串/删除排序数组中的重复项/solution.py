# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 9:34
@Desc:
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        notRepeatIdx = 0
        if len(nums) < 1:
            return notRepeatIdx
        for i in xrange(1, len(nums), 1):
            if nums[notRepeatIdx] == nums[i]:
                continue
            elif notRepeatIdx != i:
                notRepeatIdx += 1
                nums[notRepeatIdx] = nums[i]
        return notRepeatIdx + 1


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1, 1, 2])
    print s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print s.removeDuplicates([])
    print s.removeDuplicates([1])
    print s.removeDuplicates([1, 1])
    print s.removeDuplicates([1, 1, 1, 2])

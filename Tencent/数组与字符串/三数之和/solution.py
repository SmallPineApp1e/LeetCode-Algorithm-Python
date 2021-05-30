# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/29 23:03
@Desc:
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        list.sort(nums)
        length = len(nums)
        for i in xrange(0, length, 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, length - 1
            while left < right:
                threeSum = nums[left] + nums[i] + nums[right]
                if threeSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])
    print s.threeSum([])
    print s.threeSum([1])
    print s.threeSum([0, 0, 0])

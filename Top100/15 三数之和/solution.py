# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/8 22:52
@Desc: 双指针
"""


class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        res, length, i = [], len(nums), 0
        while i < length - 1:
            left, right = i + 1, length - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
            while i < length - 2 and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-1,0,1,2,-1,-4])
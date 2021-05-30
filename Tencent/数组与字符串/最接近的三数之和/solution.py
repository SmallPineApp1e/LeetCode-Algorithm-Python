# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/29 23:18
@Desc:
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res, nearestDist = 0, 2 ** 31 - 1
        list.sort(nums)
        length = len(nums)
        for i in xrange(0, length, 1):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, length - 1
            if left >= length:
                break
            while left < right:
                threeSum = nums[left] + nums[i] + nums[right]
                currDist = abs(threeSum - target)
                if currDist < nearestDist:
                    nearestDist = currDist
                    res = threeSum
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    return res
        return res


if __name__ == '__main__':
    s = Solution()
    print s.threeSumClosest([0, 2, 1, -3], 1)
    print s.threeSumClosest([-1, 2, 1, -4], 1)
    print s.threeSumClosest([1, 1, -1, -1, 3], -1)
    print s.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82)

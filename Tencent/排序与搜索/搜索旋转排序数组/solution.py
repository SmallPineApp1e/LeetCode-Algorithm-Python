# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/1 16:24
@Desc: 枚举出0-mid有旋转和没旋转的情况下right向前规约的所有条件, 其余情况就可以认为left向后规约
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif (nums[0] <= target) ^ (nums[mid] < nums[0]) ^ (target <= nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return left == right and left if nums[left] == target else -1


if __name__ == '__main__':
    s = Solution()
    print s.search([4, 5, 6, 7, 0, 1, 2], 0)
    print s.search([4, 5, 6, 7, 0, 1, 2], 3)
    print s.search([1], 0)

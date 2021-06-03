# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution2.py
@Time: 2021/6/3 19:32
@Desc:
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while True:
            idx = self.partition(nums, left, right)
            if idx == len(nums) - k:
                return nums[idx]
            elif idx > len(nums) - k:
                right = idx - 1
            else:
                left = idx + 1
        return -1

    def partition(self, nums, left, right):
        pivot, counter = left, left
        for i in xrange(left + 1, right + 1, 1):
            if nums[i] <= nums[pivot]:
                counter += 1
                if counter != i:
                    nums[counter], nums[i] = nums[i], nums[counter]
        nums[counter], nums[pivot] = nums[pivot], nums[counter]
        return counter


if __name__ == '__main__':
    s = Solution()
    print s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    print s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)

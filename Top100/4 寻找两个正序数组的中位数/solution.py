# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/4/29 20:52
@Desc: 二分指针的顶级题目
"""

import sys


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        min_int, max_int = -sys.maxint - 1, sys.maxint
        low, high, halfPartition = 0, len1, (len1 + len2 + 1) / 2
        while low <= high:
            partition1 = (low + high) / 2
            partition2 = halfPartition - partition1
            leftMax1 = min_int if partition1 == 0 else nums1[partition1 - 1]
            rightMin1 = max_int if partition1 == len1 else nums1[partition1]
            leftMax2 = min_int if partition2 == 0 else nums2[partition2 - 1]
            rightMin2 = max_int if partition2 == len2 else nums2[partition2]
            if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                leftMax = max(leftMax1, leftMax2)
                rightMin = min(rightMin1, rightMin2)
                if (len1 + len2) % 2 == 0:
                    return (leftMax + rightMin) / 2.0
                else:
                    return leftMax
            elif leftMax1 > rightMin2:
                high = partition1 - 1
            else:
                low = partition1 + 1
        return -1.0


if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1, 2], [3, 4])
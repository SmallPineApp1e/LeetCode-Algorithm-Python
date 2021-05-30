# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/5/30 15:24
@Desc:  利用三个指针，ptr1和ptr2分别指向原数组的最后一个元素，length指向合并后数组的最后一个元素，
        从后往前进行填充，数组1被填充完后，需要判断数组2是否还有元素，如果有，将其放置在nums1前面。
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2, length = m - 1, n - 1, m + n - 1
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[length] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[length] = nums2[ptr2]
                ptr2 -= 1
            length -= 1
        while ptr2 >= 0:
            nums1[length] = nums2[ptr2]
            length -= 1
            ptr2 -= 1
        print nums1


if __name__ == '__main__':
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    s.merge([1], 1, [], 0)
    s.merge([0], 0, [1], 1)

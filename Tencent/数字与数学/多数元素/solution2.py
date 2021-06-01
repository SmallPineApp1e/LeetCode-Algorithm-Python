# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution2.py
@Time: 2021/6/1 15:21
@Desc:  摩尔投票法，原理是将当前无法抵消的数字与其它不同的数字做抵消，剩下的一个数字一定是大于n/2个的数字
        可以采用major记录为当前无法抵消的数字，count记录当前无法抵消的数字有多少个，如果遇到相同的数字=>count+1
        如果遇到不同的数字则抵消一个当前数字=>count-1，如果count<0，则更换当前的数字为比对的不同的那个数字
        https://www.zhihu.com/question/49973163
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major, count = nums[0], 1
        for i in xrange(1, len(nums), 1):
            if nums[i] == major:
                count += 1
            else:
                count -= 1
            if count < 0:
                major = nums[i]
                count = 1
        return major
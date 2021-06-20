# -*- coding: utf-8 -*-

"""
@Author: SmallPineapple
@Contact: jie534838094@163.com
@Software: PyCharm
@File: solution.py
@Time: 2021/6/20 12:53
@Desc:
"""


class Solution(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        startHour = int(startTime[:2])
        startMinute = int(startTime[3:])
        if 0 < startMinute < 15:
            startMinute = 15
        elif 15 < startMinute < 30:
            startMinute = 30
        elif 30 < startMinute < 45:
            startMinute = 45
        elif startMinute > 45:
            startMinute = 0
            startHour = 0 if startHour + 1 == 24 else startHour + 1
        endHour = int(finishTime[:2])
        endMinute = int(finishTime[3:])
        if 0 < endMinute < 15:
            endMinute = 0
        elif 15 < endMinute < 30:
            endMinute = 15
        elif 30 < endMinute < 45:
            endMinute = 30
        elif startMinute > 45:
            endMinute = 45
        # print str(startHour) + " " + str(startMinute) + " " + str(endHour) + " " + str(endMinute)
        if endHour == startHour and (startMinute <= endMinute):
            return (endMinute - startMinute) / 15
        elif endHour > startHour:
            if endMinute < startMinute:
                endHour -= 1
                endMinute += 60
            return ((endHour - startHour) * 60 + (endMinute - startMinute)) / 15
        else:
            prevNight = ((23 - startHour) * 60 + (60 - startMinute)) / 15
            nextMorning = (endHour * 60 + endMinute) / 15
            return prevNight + nextMorning
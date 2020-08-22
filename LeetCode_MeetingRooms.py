# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 04:06:18 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        tempLst=sorted(intervals,key=lambda intervals:intervals[0])
        print(tempLst)
        for i in range(len(tempLst)-1):
            if tempLst[i][1]>tempLst[i+1][0]:
                return False
            
        return True
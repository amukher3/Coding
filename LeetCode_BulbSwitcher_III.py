# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 01:38:54 2020

@author: abhi0
"""

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        tempLight=sorted(light)
        cnt=0
        sum1=0
        sum2=0
        for i in range(len(light)):
            sum1=sum1+light[i]
            sum2=sum2+tempLight[i]
            if sum1==sum2:
                cnt+=1   
        return cnt
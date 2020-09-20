# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 01:59:55 2020

@author: abhi0
"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startVal=1
        cnt=startVal
        flag=0
        while True:
            flag=0
            for i in range(len(nums)):
                startVal=startVal+nums[i]
                if startVal<1:
                    flag=1
                    break
                    
            if flag==0:
                return cnt
            else:
                cnt+=1
                startVal=cnt
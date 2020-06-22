# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:52:04 2020

@author: abhi0
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 0
        
        if len(nums)>1 and len(set(nums))==1:
            return 0
        
        nums=sorted(nums)
        
        diff=[]
        for i in reversed(range(len(nums))):
            tempDiff=nums[i]-nums[0]
            diff.append(tempDiff)
            
        totSum=sum(diff)
        
        return totSum
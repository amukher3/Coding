# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:23:47 2020

@author: abhi0
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        if nums==[]:
            return None
        
        if len(nums)==1 and nums[0]==0:
            return 1
        
        minVal=0
        maxVal=max(nums)
        tempSet1=set(range(minVal,maxVal+1))
        tempSet2=set(nums)
        diffSet=tempSet1-tempSet2
        if len(diffSet)!=0:
            return list(diffSet)[0]
        else:
            return max(tempSet1)+1
        
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 08:06:54 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        leftPtr=0
        rightPtr=0
        tempLen=[]
        if nums==[]:
            return 0
        while leftPtr<=len(nums)-1 and rightPtr<=len(nums)-1:
            if sum(nums[leftPtr:rightPtr+1])<s:
                rightPtr+=1
            if sum(nums[leftPtr:rightPtr+1])>=s:
                tempLen.append(rightPtr-leftPtr+1)
                leftPtr+=1  
                
        if tempLen==[]:
            return 0
        else:
            return min(tempLen)
        
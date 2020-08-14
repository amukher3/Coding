# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:26:32 2020

@author: abhi0
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totSum=sum(nums)
        for i in range(len(nums)):
            leftSum=sum(nums[:i])
            rightSum=totSum-leftSum-nums[i]
            print(leftSum,rightSum,totSum)
            if rightSum==leftSum:
                return i
                
        return -1
            
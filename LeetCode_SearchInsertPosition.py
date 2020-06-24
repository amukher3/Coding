# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:01:02 2020

@author: abhi0
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if target==nums[i]:
                return i
            if i==0 and target<nums[i]:
                return 0
            if i==len(nums)-1 and target>nums[i]:
                return i+1
                

        for i in range(len(nums)-1):
            if target>nums[i] and target<nums[i+1]:
                return i+1
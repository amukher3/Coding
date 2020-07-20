# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 07:53:02 2020

@author: abhi0
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(nums)-1:
            if i<len(nums):
                if nums[i] in nums[i+1:]:
                    del nums[i]
                    continue
            i+=1
        return len(nums)
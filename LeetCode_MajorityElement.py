# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:22:01 2020

@author: abhi0
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                continue
            if i>0 and nums[i] in nums[:i]:
                continue
            else:
                return nums[i]
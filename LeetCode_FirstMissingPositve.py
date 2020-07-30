# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 00:45:49 2020

@author: abhi0
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if nums==[]:
            return 1
        if len(nums)==1 and nums[0]!=1:
            return 1
        if len(nums)==1 and nums[0]==1:
            return 2
        for i in range(1,max(nums)):
            if i not in nums:
                return i
        if len(list(set(list(range(1,max(nums)+1)))-set(nums)))!=0:
            return list(set(list(range(1,max(nums)+1)))-set(nums))[0]
        if len(list(set(list(range(1,max(nums)+1)))-set(nums)))==0 and 1 in nums:
             return max(nums)+1
        if len(list(set(list(range(1,max(nums)+1)))-set(nums)))==0 and 1 not in               nums:
            return 1
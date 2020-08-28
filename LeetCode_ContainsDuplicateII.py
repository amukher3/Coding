# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:12:11 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==len(list(set(nums))):
            return False
        
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                temp=nums[i+1:].index(nums[i])
                tempLen=(temp+i)+1
                print(tempLen,i)
                if abs(i-tempLen)<=k:
                    return True
        return False
        
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 05:04:46 2020

@author: abhi0
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ptr=0
        if len(nums)==1:
            return 0
        while ptr<=len(nums)-1:
            if ptr==0: 
                if nums[ptr]>nums[ptr+1]:
                    return ptr
                else:
                    ptr+=1
                    continue
            elif ptr==len(nums)-1: 
                if nums[ptr]>nums[ptr-1]:
                    return ptr
                else:
                    ptr+=1
                    continue
            elif nums[ptr]>nums[ptr+1] and nums[ptr]>nums[ptr-1]:                               
                return ptr
            ptr+=1
                
        
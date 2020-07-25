# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 00:09:52 2020

@author: abhi0
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        
        if len(nums)<=2:
            return max(nums)
        
        f=[0]*len(nums)
        f[0]=0
        f[-2]=0
        for i in range(len(nums)):
            f[i]=max(f[i-2]+nums[i],f[i-1])
            
        return f[len(nums)-1]
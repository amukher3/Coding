# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 03:27:37 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        leftPtr=0
        rightPtr=0
        k=1
        while rightPtr<=len(nums)-1:
            if nums[rightPtr]==0:
                k-=1
            if k<0:
                if nums[leftPtr]==0:
                    k+=1
                leftPtr+=1
            rightPtr+=1
        return abs(leftPtr-rightPtr)
                
        
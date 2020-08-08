# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 19:06:01 2020

@author: abhi0
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==1 and nums[0]==target:
            return [0,0]
        
        low=0
        high=len(nums)-1
       
        temp=None
        
        while low<=high:
            mid=(high+low)//2
            if target>nums[len(nums)-1]:
                return [-1,-1]
            if target<nums[0]:
                return [-1,-1]
            
            if nums[mid]==target:
                temp=mid
                break   
            if target<nums[mid]:
                high=mid-1
            if target>nums[mid]:
                low=mid+1
        
        if temp==None:
            return [-1,-1]
        
        #looking left:
        tempLeft=temp
        for i in reversed(range(0,temp)):
            if nums[i]==target:
                tempLeft=i
            else:
                break
                
        #Looking right
        tempRight=temp
        for i in range(temp+1,len(nums)):
            if nums[i]==target:
                tempRight=i
            else:
                break
        
        return [tempLeft,tempRight]
            
        
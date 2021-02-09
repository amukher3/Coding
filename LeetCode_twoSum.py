# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:12:55 2021

@author: Abhishek Mukherjee
"""

class Solution:
    def twoSum(self, nums,target) -> List[int]:
        nums1=sorted(nums)                
        left_ptr=0
        right_ptr=len(nums)-1
        
        while left_ptr<right_ptr:
            if nums1[left_ptr]+nums1[right_ptr]<target:
                left_ptr+=1
            elif nums1[left_ptr]+nums1[right_ptr]>target:
                right_ptr-=1
            elif nums1[left_ptr]+nums1[right_ptr]==target:
                temp_1=nums.index(nums1[left_ptr])
                temp_2=nums.index(nums1[right_ptr])
                if len(nums1)!=len(set(nums1)):
                    nums.pop(temp_1)
                    temp_2=nums.index(nums1[right_ptr])+1
                    return temp_1,temp_2
                else:
                    return temp_1,temp_2
                
                    
                
                    
            
            
                
                
        
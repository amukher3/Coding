# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 05:13:44 2020

@author: abhi0
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums==[]:
            return 0
        if len(nums)==1:
            return 1
        
        nums=sorted(nums)
        cnt=0
        flag=1
        temp=[]
        
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                cnt+=1
            elif nums[i+1]-nums[i]==0:
                temp.append(cnt)
                continue
            elif nums[i+1]-nums[i]>1:
                temp.append(cnt)
                cnt=0
                flag=0
        temp.append(cnt)
        return max(temp)+1
            
        
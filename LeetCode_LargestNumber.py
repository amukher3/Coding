# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:12:12 2020

@author: abhi0
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        temp=[]
        tempPrime=[]
        
        if list(set(nums))==[0]:
            return '0'
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                temp=[]
                tempPrime=[]
                temp.append(str(nums[i]))
                temp.append(str(nums[j]))
                tempPrime.append(str(nums[j]))
                tempPrime.append(str(nums[i]))
                
                temp2=int(''.join((temp)))
            
                if int(''.join(temp))>int(''.join(tempPrime)):
                    continue
                else:
                    tempSwap=nums[i]
                    nums[i]=nums[j]
                    nums[j]=tempSwap
        tempAlpha=[]           
        for i in range(len(nums)):
            tempAlpha.append(str(nums[i]))
            
        return ''.join(tempAlpha)
        
        
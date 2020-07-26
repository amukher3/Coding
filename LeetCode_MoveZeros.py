# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:53:56 2020

@author: abhi0
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zerCount=nums.count(0)
        zerVect=[0]*zerCount
        temp=[]
        for i in nums:
            if i!=0:
                temp.append(i)
        if len(temp)>0:
            for i in range(len(temp)):
                nums[i]=temp[i]
            flagCount=i
            for i in range(len(zerVect)):
                nums[flagCount+1+i]=zerVect[i]
            
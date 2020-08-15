# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 01:26:15 2020

@author: abhi0
"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        leftPtr=0
        rightPtr=len(nums)-1
        sortedNums=sorted(nums)
        flag1=0
        flag2=0
        print(nums)
        print(sortedNums)
        if nums==[]:
            return 0
        if len(nums)==1:
            return 0
        if nums==sorted(nums):
            return 0
        
        while leftPtr<=rightPtr:
            print(leftPtr,rightPtr)
            if nums[leftPtr]!=sortedNums[leftPtr] and flag1==0:
                temp1=leftPtr
                flag1=1
            if nums[rightPtr]!=sortedNums[rightPtr] and flag2==0:
                temp2=rightPtr
                flag2=1
                rightPtr-=1
            if flag1==0:
                leftPtr+=1
            if flag2==0:
                rightPtr-=1
            if flag1==1 and flag2==1:
                break
        temp=(temp2-temp1)+1
        
        return temp
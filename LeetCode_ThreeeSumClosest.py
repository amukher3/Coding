# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 04:30:57 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        
        leftPtr=0
        rightPtr=len(nums)-1
        temp=1e20
        temp=[]
        tempPrime=[]
        for i in range(leftPtr+1,rightPtr):
            leftPtr=0
            rightPtr=len(nums)-1
            diff1=target-nums[i]
            while leftPtr<rightPtr:
                temp.append([leftPtr,i,rightPtr])
                sum2=nums[leftPtr]+nums[rightPtr]
                tempPrime.append(nums[leftPtr]+nums[rightPtr]+nums[i])
                if sum2>diff1:
                    rightPtr-=1
                    if rightPtr==i:
                        rightPtr-=1
                if sum2<diff1:
                    leftPtr+=1
                    if leftPtr==i:
                        leftPtr+=1
                if sum2==diff1:
                    break
        temp1=1e20
        for i in tempPrime:
            mainDiff=abs(i-target)
            if mainDiff<temp1:
                temp1=mainDiff
                temp2=i
        return temp2
        
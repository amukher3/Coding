# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:57:31 2020

@author: abhi0
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        temp=sorted(arr)
        tempDiff=[]
        
        for i in range(len(temp)-1):
            tempDiff.append(abs(temp[i+1]-temp[i]))
            
        absDiff=min(tempDiff)
        leftPtr=0
        rightPtr=1
        tempPrime=[]
        
        while rightPtr<=len(arr)-1:
            if temp[rightPtr]-temp[leftPtr]==absDiff:
                tempPrime.append([temp[leftPtr],temp[rightPtr]])
                rightPtr+=1
            elif temp[rightPtr]-temp[leftPtr]>absDiff:
                leftPtr+=1
            if leftPtr==rightPtr:
                rightPtr+=1
            
        return tempPrime
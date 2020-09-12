# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:57:08 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        leftPtr=0
        rightPtr=1
        tempDist=[]
        
        #Edge Cases:
        if s=="":
            return 0
        if len(s)==1:
            return 1
        
        #Sliding window:
        while leftPtr<=len(s)-1 and rightPtr<=len(s)-1:
            temp=s[leftPtr:rightPtr+1]
            tempLen=len(set(temp))
            if tempLen<=2:
                rightPtr+=1
            else:
                leftPtr+=1
            tempDist.append(rightPtr-leftPtr)   
                
        return max(tempDist)
                
        
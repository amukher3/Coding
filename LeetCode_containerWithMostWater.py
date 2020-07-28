# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:43:21 2020

@author: abhi0
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPtr=0
        rightPtr=len(height)-1
        maxArea=0
        while abs(leftPtr-rightPtr)>=1:
            
            area=min(height[leftPtr],height[rightPtr])*(rightPtr-leftPtr)
            
            if area>maxArea:
                maxArea=area
                
            if height[leftPtr]<=height[rightPtr]:
                leftPtr+=1
            else:
                rightPtr-=1
                
        return maxArea        
                
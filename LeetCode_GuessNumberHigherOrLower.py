# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:34:29 2020

@author: abhi0
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low=1
        high=n 
        while low<=high:
            mid=(low+high)//2

            if guess(mid)==0:
                return mid
            
            if guess(mid)==1:
                low=mid+1
            else:
                high=mid-1
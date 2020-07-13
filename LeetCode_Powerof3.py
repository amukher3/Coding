# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 02:39:01 2020

@author: abhi0
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        rem=[]
        
        if n>0:
            if n==1 or n==3:
                return True
            
            if n==0:
                return False
            
            quo=n
            while quo>1:
                quo=round(n/3)
                rem.append(n%3)
                n=quo
                
            for i in rem:
                if i!=0:
                    return False
                continue
            
            return True 
        else:
            return False
        
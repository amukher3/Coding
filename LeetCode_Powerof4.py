# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 02:09:55 2020

@author: abhi0
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        rem=[]
        if num>0 and num<=2147483647:
            if num==1 or num==4:
                return True
            
            quo=num
            while quo>1:
                quo=round(num/4)
                rem.append(num%4)
                num=quo
                
            for i in rem:
                if i!=0:
                    return False
                continue
            return True   
        else:
            return False
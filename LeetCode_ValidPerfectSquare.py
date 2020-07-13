# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:02:03 2020

@author: abhi0
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while i**2<=num:
            if(i**2==num):
                return True
            i+=1
        return False
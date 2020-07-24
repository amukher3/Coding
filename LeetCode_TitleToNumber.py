# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:23:41 2020

@author: abhi0
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        startIdx=ord('A')-1
        sum=0
        for i in reversed(range(len(s))):
            sum=sum+(ord(s[i])-startIdx)*(26**(len(s)-(i+1)))
            
        return sum
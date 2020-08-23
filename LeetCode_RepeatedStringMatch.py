# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:04:12 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        cnt=1
        if B in A:
            return cnt
        doubleA=A
        while len(doubleA)<=len(B)+len(A):
            doubleA=doubleA+A
            cnt+=1
            if B in doubleA:
                return cnt
            
        return -1
        
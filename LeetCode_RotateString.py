# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:29:52 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A==B:
            return True
        for i in range(len(A)-1):
            temp=A[i+1:]+A[:i+1]
            if temp==B:
                return True
        return False
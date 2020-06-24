# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:58:35 2020

@author: abhi0
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack)==0 and len(needle)==0:
            return 0
        if len(haystack)!=0 and len(needle)==0:
            return 0

        k=len(needle)
        
        for i in range(0,len(haystack)):
            if haystack[i:i+k]==needle:
                return i
            
        return -1    
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:20:35 2020

@author: abhi0
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s=="":
            return 0
        
        if s==" ":
            return 1
        
        if len(s)==1:
            return 1
        
        temp=""
        tempLen=0
        
        for i in range(len(s)-1):
            for j in range(i+1,len(s)+1):
                temp=s[i:j]
                if len(temp)==len(set(temp)):
                    if len(temp)>tempLen:
                        tempLen=len(temp)
                else:
                    break
        return tempLen        
        
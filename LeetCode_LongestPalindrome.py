# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:41:41 2020

@author: abhi0
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)==0:
            return ""
        if len(s)==1:
            return s
        
        flag=0
        tempPrime=[]
        tempLen=0
        
        for i in range(len(s)-1):
            for j in range(i+1,len(s)+1):
                temp=s[i:j]
                if len(temp)>1 and temp==temp[::-1]:
                    if len(temp)>tempLen:
                        tempLen=len(temp)
                        tempPrime=temp
                        flag=1
                    
        if flag==0:
            return s[0]
        else:
            return tempPrime
                
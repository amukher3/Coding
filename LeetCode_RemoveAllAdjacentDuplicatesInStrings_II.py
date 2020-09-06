# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:42:34 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        sPrime=[]
        sPrime.extend(s)
        count=[0]*len(sPrime)
        i=0
        while i<=len(sPrime)-1:
            if i==0 or sPrime[i]!=sPrime[i-1]:
                count[i]=1
            else:
                count[i]=count[i-1]+1
                if count[i]==k:
                    sPrime[i-k+1:i+1]=""
                    i=i-k
            i+=1
            
        return ''.join(sPrime)
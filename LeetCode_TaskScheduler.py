# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 09:43:35 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies=[0]*26
        for t in tasks:
            frequencies[ord(t)-ord('A')]+=1
        frequencies=sorted(frequencies,reverse=True)
        fmax=frequencies[0]
        IdleTime=(fmax-1)*n
        for i in range(1,len(frequencies)):
            IdleTime=IdleTime-min(fmax-1,frequencies[i])
            if IdleTime<0:
                IdleTime=0
                break
        if n==0:
            return len(tasks)
        else:
            return IdleTime+len(tasks)
            
        
        
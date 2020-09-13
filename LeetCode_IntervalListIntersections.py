# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 18:47:01 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        aPtr=0
        bPtr=0
        oP=[]
        while aPtr<=len(A)-1 and bPtr<=len(B)-1:
            s1=A[aPtr][0]
            e1=A[aPtr][1]
            s2=B[bPtr][0]
            e2=B[bPtr][1]
            
            if e2>=s1 and e1>=s2:
                stPos,enPos=max(s1,s2),min(e1,e2)
                oP.append([stPos,enPos])
            if e1>e2:
                bPtr+=1
            else:
                aPtr+=1
                
        return oP      
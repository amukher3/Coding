# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 01:44:38 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        cnt=0
        tempA=[]
        tempB=[]
        if len(A)!=len(B):
            return False
        for i in range(len(A)):
            if A[i]!=B[i]:
                cnt+=1
                tempA.append(A[i])
                tempB.append(B[i])
        
        if cnt>2:
            return False
        if set(tempA)!=set(tempB):
            return False
        if A=="" and B=="":
            return False
        if A==B:
            if len(A)>=2*len(set(A)):
                print(len(A),len(set(A)))
                return True
            elif A==A[::-1] and len(A)>1:
                return True
            else:
                return False
        return True
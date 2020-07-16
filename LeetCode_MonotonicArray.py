# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:03:01 2020

@author: abhi0
"""

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A==sorted(A):
            return True

        if A==sorted(A,reverse=True):
            return True
    
        
        return False
            
##############################################
############## Real method ###################
##############################################
        
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        
        if len(A)==1:
            return True
        
        flag=0
        for i in range(len(A)-1):
            if A[i+1]>=A[i]:
                flag=1
            else:
                flag=0
                break
        if flag==1:
            return True
        
        flag=0
        for i in range(len(A)-1):
            if A[i+1]<=A[i]:
                flag=1
            else:
                flag=0
                break
        if flag==1:
            return True
        
        
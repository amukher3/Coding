# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:04:11 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        temp=[]
        tempPrime=[]
        for i in range(1,n+1):
            if temp==target:
                break
            temp.append(i)
            tempPrime.append('Push')
            if i not in target:
                temp.pop()
                tempPrime.append('Pop')    
        return tempPrime
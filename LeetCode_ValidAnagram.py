# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 07:26:57 2020

@author: abhi0
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s==t:
            return True
        
        tempS=[]
        tempS.extend(s)
        tempT=[]
        tempT.extend(t)
        if len(tempS)>len(tempT):
            for i in range(len(tempS)):
                if tempS[i] in tempT:
                    tempT.remove(tempS[i])
                else:
                    return False
            return True
        else:
            for i in range(len(tempT)):
                if tempT[i] in tempS:
                    tempS.remove(tempT[i])
                else:
                    return False
            return True
            
        
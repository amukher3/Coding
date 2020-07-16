# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 08:39:36 2020

@author: abhi0
"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        if s==t:
            return False
        
        if len(s)-len(t)>1:
            return False
        if len(t)-len(s)>1:
            return False
        
        temp=[]
        tempPrime=[]
        temp.extend(s)
        tempPrime.extend(t)
        
        #Delete a character
        for i in range(len(temp)):
            temp.pop(i)
            if temp==tempPrime:
                return True
            temp=[]
            temp.extend(s)
            
        temp=[]
        tempPrime=[]
        temp.extend(s)
        tempPrime.extend(t)
        #Insert a character:
        for i in range(len(tempPrime)):
            temp.insert(i,tempPrime[i])
            if temp==tempPrime:
                return True
            temp=[]
            temp.extend(s)
        
        temp=[]
        tempPrime=[]
        temp.extend(s)
        tempPrime.extend(t)      
        #Replace a character:
        for i in range(len(temp)):
            temp.pop(i)
            if i<len(tempPrime):
                temp.insert(i,tempPrime[i])
                if temp==tempPrime:
                    return True
                temp=[]
                temp.extend(s)

            
        return False
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:55:21 2020

@author: abhi0
"""

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S=S.upper()
        temp=re.split('',S)
        
        tempCount=temp.count('-')
        for i in range(tempCount):
            temp.remove('-')
            
        tempCount=temp.count('')
        for i in range(tempCount):
            temp.remove('')    
        
        temp.reverse()
        tempPrime=[]
        
        for i in range(0,len(temp),K):
            tempPrime.append(temp[i:i+K])
            
        tempTilda=[]
        for i in tempPrime:
            tempTilda.append(''.join(i))
            
        str1='-'.join(tempTilda)
        
        return str1[::-1]
        
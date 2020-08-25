# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 02:50:21 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        tempDict=dict()
        tempS=[]
        tempS.extend(s)
        for i in set(tempS):
            cnt=tempS.count(i)
            tempDict.update({i:cnt})
            
        flag=0
        cntPrime=0
        
        for key,values in tempDict.items():
            if values%2!=0:
                cntPrime+=(values-1)
                flag=1
            else:
                cntPrime+=values
    
        if flag==1:
            return cntPrime+1
        else:
            return cntPrime
        
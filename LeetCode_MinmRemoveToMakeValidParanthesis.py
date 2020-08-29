# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:01:37 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp=[]
        sPrime=[]
        sPrime.extend(s)
        temp1=[]
        i=0
        while i<=len(sPrime)-1:
            if sPrime[i]==')' and temp==[]:
                sPrime.remove(')')
                continue
            elif sPrime[i]=='(':
                temp.append('(')
                temp1.append(i)
            elif sPrime[i]==')' and temp!=[]:
                temp.pop() 
                temp1.pop()
            i+=1
            
        i=0    
        while i<=len(temp1)-1:
            sPrime[temp1[i]]=''
            i+=1
            
        return ''.join(sPrime)

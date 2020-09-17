# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:46:47 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def makeGood(self, s: str) -> str:
        temp=[]
        i=0
        flag=0
        while i<=len(s)-1:
            if temp!=[]:
                if (temp[len(temp)-1].islower() and s[i]==temp[len(temp)-1].upper()) or (s[i].islower() and s[i].upper()==temp[len(temp)-1]):
                    temp.pop()
                else:
                    temp.append(s[i])
            else:
                temp.append(s[i])
                
            i+=1
            
        return ''.join(temp)
                
                
        
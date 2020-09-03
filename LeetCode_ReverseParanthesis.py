# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:21:49 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        temp=[]
        for i in s:
            if i==')':
                tempPrime=[]
                for j in range(len(temp[::-1])):
                    tempPrime.append(temp[::-1][j])
                    if tempPrime[j]=='(':
                        break
                for k in range(len(tempPrime)-1):
                    temp[len(temp)-j-1]=tempPrime[k]
                    j-=1
                temp=temp[:-1]
            else:
                temp.append(i)
                
        return ''.join(temp)
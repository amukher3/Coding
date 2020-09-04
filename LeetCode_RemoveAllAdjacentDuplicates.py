# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:27:44 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        temp=[]
        for i in S:
            if len(temp)>0 and i==temp[len(temp)-1]:
                temp.pop()
                continue
            temp.append(i) 
        return ''.join(temp)

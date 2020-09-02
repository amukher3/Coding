# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:39:35 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        temp=[]
        cnt=0
        for  i in S:
            if i=='(':
                temp.append('(')
            elif i==')' and len(temp)!=0:
                temp.pop()
            elif i==')' and len(temp)==0:
                cnt+=1
        return len(temp)+cnt
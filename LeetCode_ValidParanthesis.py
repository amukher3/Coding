# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:59:18 2020

@author: abhi0
"""

class Solution:
    def isValid(self, s: str) -> bool:
        tempLst=[]
        temp=0
        if s==']' or s=='}' or s==')':
            return False
        for i in s:
            if i=='(' or i=='{' or i=='[':
                tempLst.append(i)
            if (i==')' or i=='}' or i==']') and len(tempLst)!=0:
                temp=tempLst.pop()
            if i==')' and temp!='(':
                return False
            if i=='}' and temp!='{':
                return False
            if i==']' and temp!='[':
                return False
            continue
            
        if len(tempLst)==0:
            return True
        
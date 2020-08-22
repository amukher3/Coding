# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:23:31 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        roundPts=[]
        for i in range(len(ops)):
            if ops[i].isdigit() is True or len(ops[i])>1:
                roundPts.append(int(ops[i]))
            elif ops[i]=='C':
                roundPts.pop(len(roundPts)-1)
            elif ops[i]=='+':
                roundPts.append(roundPts[len(roundPts)-1]+roundPts[len(roundPts)-2])
            elif ops[i]=='D':
                roundPts.append(2*roundPts[len(roundPts)-1])       
        return sum(roundPts)
                
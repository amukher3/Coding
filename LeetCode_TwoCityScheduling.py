# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 03:51:11 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        tempLst=list(sorted(costs,key=lambda costs:costs[0]-costs[1]))
        citA=0
        citB=0
        for i in range(len(tempLst)):
            if i<len(costs)/2:
                citA+=tempLst[i][0]
        
        for i in range(len(tempLst)):
            if i>=len(costs)/2:
                citB+=tempLst[i][1]
        
        return citA+citB
        
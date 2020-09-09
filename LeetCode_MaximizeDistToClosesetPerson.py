# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 00:17:45 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        idx=[]
        idx1=[]
        for i in range(len(seats)):
            if seats[i]==0:
                idx.append(i)
            if seats[i]==1:
                idx1.append(i)  
        tempVal=[] 
        if len(idx1)<=1:
            tempVal.append((len(seats)-1)-idx1[0])
            tempVal.append((idx1[0]-0))
        else:
            for i in range(len(idx1)-1):
                temp=idx1[i+1]-idx1[i]
                tempVal.append(temp//2)
        
        #to take care of the edge
        #case,i.e if the 1st or last is
        #empty. Then take the dist. between 
        #that and the next non-empty seat or
        #the other way around. 
        
        if 0 not in idx1:
            tempVal.append(idx1[0]-0)
        if len(seats)-1 not in idx1:
            tempVal.append((len(seats)-1)-idx1[len(idx1)-1])
            
        return (max(tempVal))
            
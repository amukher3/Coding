# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:16:54 2020

@author: Abhishek Mukherjee
"""

#Merge overlapping intervals...
#Leetcode problem

class Solution:
    def merge(self, intervals):
        arr=intervals
        i=0
        arr.sort()
        while i<=len(arr)-1:
            LB1=arr[i][0]
            UB1=arr[i][1]
            if(i<=len(arr)-2):
                LB2=arr[i+1][0]
                UB2=arr[i+1][1]
                #if(LB2<=UB1 and UB1!=LB1 and UB2!=LB2):
                if(LB2<=UB1):    
                    #Overlapped case
                    minLB=min(LB1,LB2)
                    maxUB=max(UB1,UB2)
                    arr[i][0]=minLB
                    arr[i][1]=maxUB
                    arr.pop(i+1)
                    continue
                else:
                    #Non-overlapping case
                    #move the pointer to the 
                    #next list.
                    i+=1
                continue
            break
            
        return arr
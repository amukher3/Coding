# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:59:29 2020

@author: Abhishek Mukherjee
"""
class Solution:
    def subsets(self, nums: List[int]):
        from itertools import combinations 
        #arr=[1,2,3]
        FinList=[]
        tempList=[]
        arr=nums
        for i in range(len(arr)):
            tempList=list(list(combinations(arr,i+1)))
            #Removing duplicates
            tempList=list(set(tempList))
            #Appending to the final list after
            #changing the tuples to list
            for j in range(len(tempList)):
                FinList.append(list(tempList[j]))
                #tempList=[]
        FinList.append([]) 
        
        return FinList
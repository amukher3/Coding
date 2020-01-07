# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 18:35:24 2020

@author: Abhishek Mukherjee
"""

#arr=['a','a','b','a','c','d','b']

class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        arr=nums
        
        CountDict={}
       
        for i in arr:
            if i not in CountDict.keys():
                CountDict[i]=1
            else:
                CountDict[i]+=1  
        sortedDict=sorted(CountDict.items(),key=lambda x: x[1],reverse=True) 
        FinalList=[]
        for i in range(k):
            FinalList.append(sortedDict[i][0])
            
            
        return FinalList            
        
    

       



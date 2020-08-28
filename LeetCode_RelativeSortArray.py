# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:06:52 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        tempCount=[]
        tempEle=[]
        for i in arr2:
            tempCount.append(arr1.count(i))
            tempEle.append(i)
    
        tempArr=[]
        for i in range(len(tempEle)):
            for j in range(tempCount[i]):
                tempArr.append(tempEle[i])
                
        tempEx=[]
        for i in arr1:
            if i not in tempArr:
                tempEx.append(i)
        return (tempArr+sorted(tempEx))

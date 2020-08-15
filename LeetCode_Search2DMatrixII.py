# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 04:47:24 2020

@author: abhi0
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        temp=[]
        for i in range(len(matrix)):
            temp.extend(matrix[i])
        
        temp=sorted(temp)
        low=0
        high=len(temp)-1
        mid=(low+high)//2
        while low<=high:
            mid=(low+high)//2
            if target==temp[mid]:
                return True
            if temp[mid]>target:
                high=mid-1
            if temp[mid]<target:
                low=mid+1
            
            
        return False
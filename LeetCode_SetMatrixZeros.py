# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:22:52 2020

@author: abhi0
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        temp=[]
        tempPrime=[]
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                temp.append(i)
                for j in range(len(matrix[i])):
                    if matrix[i][j]==0:
                        tempPrime.append(j)
                        
        for i in temp:
            matrix[i]=[0]*len(matrix[i])
        
        for j in tempPrime:
            for i in range(len(matrix)):
                matrix[i][j]=0
            
            
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:48:14 2020

@author: abhi0
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i==j:
                    for m in range(i,len(matrix)):
                        temp=matrix[i][m]
                        matrix[i][m]=matrix[m][i]
                        matrix[m][i]=temp
                    
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
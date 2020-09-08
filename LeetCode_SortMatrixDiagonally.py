# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:47:42 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        temp=[]
        tempDict={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i-j) not in tempDict.keys():
                    tempDict.update({(i-j):str(mat[i][j])})
                else: 
                    tempDict[i-j]=tempDict[i-j]+" "+(str(mat[i][j]))
        
        for key,vals in tempDict.items():
            tempVals=tempDict[key]
            temp1=tempVals.split(' ')
            temp2=[]
            for i in temp1:
                temp2.append(int(i))
            tempDict.update({key:sorted(temp2)})
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j]=tempDict[i-j][0]
                tempDict[i-j].pop(0)
                 
        return mat
                
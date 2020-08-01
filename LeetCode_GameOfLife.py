# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:59:40 2020

@author: abhi0
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        arr=board
        tempArr=[[]]*len(arr)
        for m in range(len(arr)):
    
            tempArr[m]=[0]*len(arr[m])
    
            for n in range(len(tempArr[m])):
                temp=[]
                tempPrime=[]
                M=len(arr)

                if m>=M-1:
                    temp1=M
                else:
                    temp1=m+2
                    
                for i in range(m-1,temp1):
                    N=len(arr[i])
                    for j in range(n-1,n+2):
                        if i==m and j==n:
                            continue
                        if i<M and i>=0 and j<N and j>=0:  
                            tempPrime.append(i)
                            tempPrime.append(j)
                            temp.append(arr[i][j])

            
                countIdx=temp.count(1)
                countIdxPrime=temp.count(0)
        
                print(countIdx)

                if arr[m][n]==1 and countIdx<2:
                    tempArr[m][n]=0
                    continue
                if arr[m][n]==1 and (countIdx==2 or countIdx==3):
                    tempArr[m][n]=1
                    continue
                if arr[m][n]==1 and countIdx>3:
                    tempArr[m][n]=0
                    continue
                if arr[m][n]==0 and countIdx==3:
                    tempArr[m][n]=1
                    continue
            
            
        for i in range(len(tempArr)):
            for j in range(len(tempArr[i])):
                arr[i][j]=tempArr[i][j]
        
        
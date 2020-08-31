# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:45:34 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        tempStack=[]
        idxStack=[]
        temp=[]
        rightPtr=len(T)-1
        flag=0
        while rightPtr>0:
           tempStack.append(T[rightPtr])
           idxStack.append(rightPtr)
           rightPtr-=1
           for j in reversed(range(len(tempStack))):
                if T[rightPtr]>=tempStack[j]:
                    tempStack.pop()
                    idxStack.pop()
                    flag=0
                elif T[rightPtr]<tempStack[j]:
                    temp.append(idxStack[j]-rightPtr)
                    flag=1
                    break
           if flag==0:
                temp.append(0)
        return temp[::-1]+[0]
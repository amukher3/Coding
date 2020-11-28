# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:25:22 2020

@author: abhi0
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust==[]:
            if N==1:
                return N
            else:
                return -1
        
        trustDict=dict()
        for i in trust:
            if i[0] not in trustDict.keys():
                trustDict.update({i[0]:[i[1]]})
            else:
                trustDict[i[0]].append(i[1])
                                                       
        totRange=list(range(1,N+1))
        tempLst=list(set(list(trustDict.keys())))
        tempVal=list(trustDict.values())
        temp=[]
        for i in totRange:
            if i not in tempLst:
                temp.append(i)
                
        count=0
        for j in temp:
            if j not in trustDict.keys():
                for k in tempVal:
                    if j in k:
                        count+=1
        if count==len(trustDict.keys()):
            return j
        else:
            return -1
                
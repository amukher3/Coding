# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:59:42 2020

@author: abhi0
"""

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items=sorted(sorted(items),reverse=True)
        countDict=dict()
        scoreDict=dict()
        for i in range(len(items)):
            if items[i][0] not in countDict.keys() and items[i][0] not in        scoreDict.keys():
                countDict.update({items[i][0]:1})
                scoreDict.update({items[i][0]:items[i][1]})
            else:
                if countDict[items[i][0]]<5:
                    scoreDict[items[i][0]]+=items[i][1]
                    countDict[items[i][0]]+=1
                    
        
        tempTup=sorted(scoreDict.items(),key=lambda x:x[0])    
        
        temp=[]            
        temp=[]
        for i,j in tempTup:
            tempVal=int(j/5)
            temp.append([i,tempVal])
        return temp
    
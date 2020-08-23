# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:03:42 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words=sorted(words)
        tempDict=dict()
        for i in words:
            if i not in tempDict.keys():
                tempDict.update({i:1})
            else:
                tempDict[i]+=1
        
        tempDict=sorted(tempDict.items(),key=lambda tempDict:tempDict[1],reverse=True)
        
        tempLst=[]
        for i in range(len(tempDict)):
            if i==k:
                break
            else:
                tempLst.append(tempDict[i][0])   
                
        return tempLst
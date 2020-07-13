# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:50:08 2020

@author: abhi0
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        tempDict=dict()
        for i in s:
            if i in tempDict.keys():
                tempDict[i]+=1
            else:
                tempDict.update({i:1}) 
                
        for key,val in tempDict.items():
            if val==1:
                idx=s.index(key)
                return idx
            
        return -1
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:02:02 2020

@author: abhi0
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteDict=dict()
        
        for i in ransomNote:
            if i not in noteDict.keys():
                noteDict.update({i:1})
            else:
                noteDict[i]+=1
                
        for key,val in noteDict.items():
            tempCount=magazine.count(key)
            if tempCount>=val:
                continue
            else:
                return False
        return True
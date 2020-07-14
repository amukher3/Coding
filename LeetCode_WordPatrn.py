# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:22:25 2020

@author: abhi0
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        flag=0
        tempDict=dict()
        tempStr=str.split(' ')
        
        if len(tempStr)!=len(pattern):
            return False
        
        
        for i in range(len(pattern)):
            if pattern[i] not in tempDict.keys():
                tempDict.update({pattern[i]:tempStr[i]})
            else:
                if tempDict[pattern[i]]!=tempStr[i]:
                    flag=1
                    return False
                continue
                flag=0
        
        
        tempDict=dict()
        for i in range(len(tempStr)):
            if tempStr[i] not in tempDict.keys():
                tempDict.update({tempStr[i]:pattern[i]})
            else:
                if tempDict[tempStr[i]]!=pattern[i]:
                    flag=1
                    return False
                continue
                flag=0
                
        
        if flag==0:
            return True
                
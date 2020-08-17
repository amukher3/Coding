# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 19:47:30 2020

@author: abhi0
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        tempDict=dict()
        posDict=dict()
        for i in range(len(s)):
            if s[i] in tempDict:
                tempDict[s[i]]+=1
                posDict[s[i]].append(i)
            else:
                tempDict.update({s[i]:1})
                posDict.update({s[i]:[i]})
                
        tempDict2=dict()
        posDict2=dict()
        for i in range(len(t)):
            if t[i] in tempDict2:
                tempDict2[t[i]]+=1
                posDict2[t[i]].append(i)
            else:
                tempDict2.update({t[i]:1})
                posDict2.update({t[i]:[i]})
                        
        tempVals1=list(tempDict.values())
        tempVals2=list(tempDict2.values())
    
        posVals1=list(posDict.values())
        posVals2=list(posDict2.values())
        
        if tempVals1==tempVals2:
            if posVals1==posVals2:
                return True
        else:
            return False
        
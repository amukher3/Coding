# -*- coding: utf-8 -*-

class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanDict={'I':1,
                  'V':5,
                  'X':10,
                  'L':50,
                  'C':100,
                  'D':500,
                  'M':1000}
        
        temp=re.split('',s)
        intVal=[]
        
        for i in range(len(temp)):
            if temp[i] in romanDict.keys():
                intVal.append(romanDict[temp[i]])
                
        cumSum=0  
        for i in range(len(intVal)-1):
            if intVal[i+1]>intVal[i]:
                cumSum=cumSum-intVal[i]
            else:
                cumSum=cumSum+intVal[i]
        return cumSum+intVal[len(intVal)-1]
                
            
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:07:30 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letLog=[]
        digLog=[]
        
        for i in range(len(logs)):
            temp=[]
            temp=logs[i].split(' ')
            if temp[1].isdigit() is True:
                digLog.append(logs[i])
            else:
                letLog.append(logs[i])
                
        tempLetLog=[]        
        for i in letLog:
            tempLetLog.append(' '.join(i.split(' ')[1:]+[i.split(' ')[0]]))
            
        tempLetLog=sorted(tempLetLog)
        letLog=[]
        for i in tempLetLog:
            tempPrime=i.split(' ')[:-1]
            temp=i.split(' ')[-1]
            letLog.append(' '.join([temp]+tempPrime))
            
        return letLog+digLog
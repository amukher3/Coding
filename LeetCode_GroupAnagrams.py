# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:28:10 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tempLst=[]
        tempDict=dict()
        tempDict=[dict() for i in range(len(strs))]
        for i in range(len(strs)):
            for j in strs[i]:
                if j in tempDict[i].keys():
                    tempDict[i][j]+=1
                else:
                    tempDict[i].update({j:1}) 
        
        temp=[]
        for i in range(len(tempDict)):
            tempDict[i]=sorted(tempDict[i].items(),key=lambda i:i[0])
        
        temp1=[]
        temp2=[]
        temp3=[]
        for i in range(len(tempDict)-1):
            temp1=[]
            for j in range(i+1,len(tempDict)):
                if tempDict[i]==tempDict[j]:
                    if strs[j] not in temp3:
                        temp1.append(strs[j])
            if strs[i] not in temp3:
                temp1.append(strs[i])       
                temp2.append(temp1)
            temp3.extend(temp1)
            
        for i in strs:
            if i not in temp3:
                temp2.append([i])
                
        return temp2
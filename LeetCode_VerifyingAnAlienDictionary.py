# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:58:29 2020

@author: abhi0
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        tempDict=dict()
        for i in range(len(order)):
            if order[i] not in tempDict:
                tempDict.update({order[i]:i+1})
        
        #for the end-0f-word letter:
        tempDict.update({'#':0})
        
        for i in range(len(words)-1):
            temp=words[i]+'#'
            tempPrime=words[i+1]+'#'
            print(temp,tempPrime)
            j=0
            while j<len(min(temp,tempPrime)):
                if tempDict[temp[j]]<tempDict[tempPrime[j]]:
                    break
                if tempDict[temp[j]]==tempDict[tempPrime[j]]:
                    j+=1
                    continue
                if tempDict[temp[j]]>tempDict[tempPrime[j]]:
                    return False 
        return True
                    
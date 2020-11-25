# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:35:53 2020

@author: abhi0
"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        strLengths=list(map(lambda x:len(x),A))
        idx=strLengths.index(min(strLengths))
        strs=A[idx]
        temp=[]
        countPrime=0
        for characs in strs:
            count=0
            for i in range(len(A)):
                tempWords=[]
                tempWords.extend(A[i])
                if characs in tempWords:
                    tempWords.remove(characs)
                    count+=1
                    if count==len(A):
                        temp.append(characs)
                    A[i]=''.join(tempWords)
                    continue
                else:
                    break    
            countPrime+=1        
        return temp            
        
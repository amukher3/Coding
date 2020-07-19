# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 05:46:52 2020

@author: abhi0
"""

class Solution:
    def compress(self,chars):
        
        
        if len(chars)==1:
            return 1
        
        tempPrime=[]
        temp=[]
        flag=0
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                temp.append(chars[i])
                if i>=len(chars)-2:
                    tempPrime.append(temp)
                    flag=1
            else:
                temp.append(chars[i])
                if flag!=1:
                    tempPrime.append(temp)
                temp=[]
                
    
        if chars[len(chars)-1]==tempPrime[len(tempPrime)-1][0]:
            tempPrime[len(tempPrime)-1].append(chars[len(chars)-1])
        else:
            tempPrime.append([chars[len(chars)-1]])
    
        temp=[]
        tempTilda=[]
        for i in range(len(tempPrime)):
            temp=tempPrime[i]
            tempLen=len(temp)
            tempTilda.append(str(temp[0]))
            if tempLen>9:
                for j in range(len(str(tempLen))):
                    tempTilda.append(str(tempLen)[j])
            else:  
                if tempLen>1:
                    tempTilda.append(str(tempLen))
                
        for i in range(len(tempTilda)):
            chars[i]=tempTilda[i]   
            
        del chars[len(tempTilda):]
        
    
    
        return len(tempTilda)
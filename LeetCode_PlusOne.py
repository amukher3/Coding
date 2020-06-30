# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:33:28 2020

@author: abhi0
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        tempTilda=''
        for i in digits:
            tempTilda=tempTilda+str(i)
            
        temp=re.split('',tempTilda)
        temp=temp[1:len(temp)-1]

        sumIp=1
        sumOp=[]
        carOp=[]
        carFlag=1

        for i in reversed(temp):
    
            if sumIp==1 and carFlag==1:
                tempPrime=int(i)+1
            else:
                tempPrime=int(i)
        
            if tempPrime>9:
                sumOp.append(0)
                carOp.append(1)
                carFlag=1
                sumIp=1
            else:
                sumOp.append(tempPrime)
                carOp.append(0)
                carFlag=0
                sumIp=0

        totSum=[]        
        if carOp[len(carOp)-1]==1:
            totSum.append(carOp[len(carOp)-1])
            totSum.extend(sumOp)
            print(totSum)
        else:
            totSum.extend(sumOp[::-1])
        
        return totSum
            
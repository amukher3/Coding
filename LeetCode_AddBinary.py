# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:10:26 2020

@author: abhi0
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        tempA=re.split('',a)[1:-1]
        tempB=re.split('',b)[1:-1]

        if len(tempA)>len(tempB):
            temp=['0']*(len(tempA)-len(tempB))
            temp.extend(tempB)
            tempB=[]
            tempB=temp
        else:
            temp=['0']*(len(tempB)-len(tempA))
            temp.extend(tempA)
            tempA=[]
            tempA=temp
    
        lenTempA=len(tempA)
        lenTempB=len(tempB)
    
        def exOr(temp1,temp2,temp3):
            tempArr=[temp1,temp2,temp3]
            tempPrime=tempArr.count(1)
            print(tempPrime)
            if tempPrime%2==0:
                return 0
            else:
                return 1
    
        def Oring(temp1,temp2,temp3):
            tempArr=[temp1,temp2,temp3]
            if 1 in tempArr:
                return 1
            else:
                return 0
    
        S_op=[]
        C_op=[]
        Cin=0

        for i in reversed(range(lenTempB)):
            
            S_op.append(exOr(int(tempB[i]),int(tempA[i]),int(Cin))) 
            tempExp1=int(tempA[i])*int(tempB[i])
            tempExp2=int(tempB[i])*int(Cin)
            tempExp3=int(Cin)*int(tempA[i])
            temp=Oring(tempExp1,tempExp2,tempExp3)  
            C_op.append(temp)
            Cin=temp

        tempPrime=[]
        tempPrime=[]
        if Cin==1:
            tempPrime.append(Cin)
            tempPrime.extend(S_op[::-1])
        else:
            tempPrime.extend(S_op[::-1])

        tempLst=list(map(lambda temp:str(temp),tempPrime))
        return ''.join(tempLst)
        
        
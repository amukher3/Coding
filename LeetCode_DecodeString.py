# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 04:40:43 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def decodeString(self, s: str) -> str:
        tempNum=[]
        tempAlpha=[]
        tempPrime=[]
        temp3=[]
        flagPrime=1
        tempNum1=""
        for i in s:
            if i.isdigit() and flagPrime==1:
                tempNum1=tempNum1+i
                flagPrime=1
                continue
            if tempNum1!="":
                tempNum.append(tempNum1)
                tempNum1=""
            if i=='[' or i.isalpha():
                tempAlpha.append(i)
            if i==']':
                temp1=tempNum.pop()
                temp3=[]
                while True:
                    temp2=tempAlpha.pop()
                    if temp2=='[':
                        break
                    else:
                        temp3.append(temp2)
            
                for i in range(int(temp1)):
                    tempAlpha.extend(temp3[::-1])
           
        return ''.join(tempAlpha)
                
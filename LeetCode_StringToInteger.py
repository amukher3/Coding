# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 01:58:05 2020

@author: abhi0
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        if str=="-":
            return 0
        temp=[]
        str=str.strip(' ')
        if str=="":
            return 0
        flag=0
        flagPrime=0
        flagAlpha=0
        for i in str:
            if i=='+' and flag==0 and flagAlpha==0:
                temp.append('0')
                flag=1
                continue
            if i=='-' and flag==0 and flagAlpha==0:
                temp.append('-')
                flag=1
                continue
            if i.isdigit() is False and flagAlpha==1:
                #You have alrady encountered a  digit 
                #and are now encountering a alpha...
                break
            if i.isdigit() is False and flagAlpha==0:
                #You have not encountered any digit yet
                #but are encounterinig alphabets so
                # append 0 and break
                temp.append('0')
                break
            if i.isdigit() is True:
                temp.append(i)
                flagAlpha=1
            else:
                temp.append('0')
                
        tempPrime=int(''.join(temp))
        if tempPrime>2**31-1:
            return 2**31-1
        if tempPrime<-2**31:
            return -2**31
        return tempPrime
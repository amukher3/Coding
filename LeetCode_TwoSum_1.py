# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:19:06 2019

@author: Abhishek Mukherjee
"""

list_a=[3,2,3]

target = 6
sumList=[]

for i in range(len(list_a)):
    for j in range(i+1,len(list_a)):
        temp=i
        temp1=j
#        if temp==temp1 and temp1!=0 and temp!=0:
#            del list_a[temp1]
#            temp1=list_a.index(temp)
        if(list_a[temp]+list_a[temp1]==target and temp not in sumList and temp1 not in sumList):
            sumList.append(temp)
            sumList.append(temp1)
            
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 17:03:56 2019

@author: Abhishek Mukherjee
"""
import math
import os
import random
import re
import sys

from collections import OrderedDict
letter = dict()

if __name__ == '__main__':
    name = str(input())
    
    
    for i in name:
        letter.setdefault(i, 0)
        letter[i]+=1
        
        sortedLetterValues=sorted(set(letter.values()),reverse=True)
        listOfKeys = list()
        listOfItems = letter.items()
    for j in range(len(sortedLetterValues)): 
        temp=[]
        for item in listOfItems:
            if item[1] == sortedLetterValues[j]:
                temp.append(item[0])
                
        listOfKeys.append(temp)
        
    for i in range(len(listOfKeys)):
        if len(listOfKeys[i])>1:
           listOfKeys[i][:]=sorted(listOfKeys[i])
            
    from functools import reduce
    import operator
    listOfKeys=reduce(operator.concat, listOfKeys)
    
    firstThreeKeys=listOfKeys[0:3]
    
    tempList=list(letter.values())
    valList=[]
    for i in range(len(firstThreeKeys)):
        Idx=list(letter.keys()).index(firstThreeKeys[i])
        valList.append(tempList[Idx])
        
    for i in range(len(firstThreeKeys)):
        print(*firstThreeKeys[i],valList[i])
        
    
                   
                
   
        
    

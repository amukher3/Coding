# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:48:47 2020

@author: abhi0
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    tempDict=dict()
    for i in s:
        if i not in tempDict.keys():
            tempDict.update({i:1})
        else:
            tempDict[i]+=1
    tempVals=list(tempDict.values())
    if len(set(list(tempDict.values())))==1:
        return 'YES'
    if len(set(list(tempDict.values())))>1:
        if len(set(tempVals))==2 and min(tempVals)==1 and tempVals.count(min(tempVals))==1:
            return "YES"
        if tempVals.count(min(tempVals))>1 and tempVals.count(min(tempVals))<len    (tempVals)-1:
            return "NO"
        if max(tempVals)>1:
            if max(tempVals)-1==min(tempVals):
                return 'YES'
            else:
                return "NO"
        

        
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

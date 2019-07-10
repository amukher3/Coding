# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 01:15:01 2019

@author: Abhishek Mukherjee
"""

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
     arr=[]
     for i in range(1,n+1):
        arr.append(0)
        
     for i in range(m):
        
        tempPrime=[]
        stPos=queries[i][0]
        enPos=queries[i][1]
        val=queries[i][2]
        val=[val]*(enPos-stPos+1)
        from operator import add
        tempPrime[0:stPos-1]=[0]*((stPos-1)-0)  
        tempPrime[stPos:enPos+1]=val
        tempPrime[enPos+1:n+1]=[0]*((n-enPos)-0)
        arr=list( map(add, arr, tempPrime) )

     return max(arr)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

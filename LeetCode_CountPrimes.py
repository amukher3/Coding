# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 23:45:21 2020

@author: abhi0
"""

class Solution:
    def countPrimes(self, n: int) -> int:
      #O(N^1.5)
      tempLst=[True]*(n-1)
        
      for i in range(2,round(sqrt(n))+1):
            for j in range(i,n,i):
                if j!=i:
                    tempLst[j-1]=False
      tempPrime=tempLst[1:]
      return tempPrime.count(True)
    
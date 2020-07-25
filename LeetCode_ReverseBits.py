# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:56:11 2020

@author: abhi0
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        tempPrime=bin(n)
        tempLen=len(str(tempPrime[2:]))
        temp='0'*(32-tempLen)+str(tempPrime[2:])
        return int(temp[::-1],2)
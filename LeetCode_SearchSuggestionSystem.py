# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 00:05:35 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products=sorted(products)
        tempPrime=[]
        for i in range(len(searchWord)):
            temp=searchWord[:i+1]
            cnt=0
            tempProds=[]
            for j in products:
                if cnt==3:
                    break
                if temp==j[:i+1]:
                    tempProds.append(j)
                    cnt+=1
            tempPrime.append(tempProds)    
        return (tempPrime)
            
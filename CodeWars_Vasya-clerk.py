# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:16:56 2019

@author: amukher3
"""




def tickets(people):
    
    
    CostVec=people
    tempChange=0
    NetChange=0
    TicPrice=25
    c=0

    for i in range(len(CostVec)):
        if CostVec[i]==TicPrice:
            NetChange=NetChange+TicPrice
        elif CostVec[i]>TicPrice and NetChange>CostVec[i]-TicPrice:
                tempChange=CostVec[i]-TicPrice
                NetChange=NetChange+tempChange
        else:
            
            c=1
            break

    if c==0:        
        return "YES"
    else:
        return "NO"



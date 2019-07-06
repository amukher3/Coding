# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:56:28 2019

@author: Abhishek Mukherjee
"""



#n for number of items
n=list(map(int, input()))

ItemIndex=[]
PriceIndex=[]

for i in range(n[0]):
    lst=list(map(str, input().split())) 
    
    
    Item=lst[0:len(lst)-1]
    Item=" ".join(Item)
    
    Price=lst[-1:]
    Price=" ".join(Price)
    
    if Item in ItemIndex:
       Idx=ItemIndex.index(Item)
       PriceIndex[Idx]=PriceIndex[Idx]+int(Price)

    else:
       ItemIndex.append(Item)
       PriceIndex.append(int(Price))
    
for i,j in range(len(ItemIndex)):
    print(ItemIndex[i],PriceIndex[i])    
   
    


# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:21:59 2019

@author: Abhishek Mukherjee
"""

s='omg world lol'

Idx=[]
NameLst=list(s)
for i in range(len(NameLst)):
    if s[i]==" ":
        Idx.append(i)
        
c=NameLst[0].upper()
NameLst[0]=c
for i in range(len(Idx)):
    d=NameLst[Idx[i]+1].upper()
    NameLst[Idx[i]+1]=d

FinalName="".join(NameLst)
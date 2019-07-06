# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:40:27 2019

@author: Abhishek Mukherjee
"""

#Size of set A ~~~ M
M=list(map(int, input()))

#list A
listA=list(map(int, input().split()))

#Size of set B ~~~ N
N=list(map(int, input()))

#list B
listB=list(map(int, input().split()))

#Set A
setA=set()

#SetB
setB=set()

for i in range(M[0]):
    setA.add(listA[i])
    
    
for i in range(N[0]):
    setB.add(listB[i])

setC=set()    
#SetC -- diff set
setC1=setA.difference(setB)
setC2=setB.difference(setA)
setC=setC1.union(setC2)

setC=sorted(setC)

for i in range(len(setC)):
    print(setC[i])


    
    



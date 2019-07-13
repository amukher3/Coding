# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 00:33:16 2019

@author: Abhishek Mukherjee
"""
##############################################################################
##################### My method #############################################
# the number of words
n=int(input())
inpWord=[]
wrdLst=[]

#input strings
for i in range(n):
    inpWord.append(str(input()))
    
for i in range(len(inpWord)):
    if inpWord[i] not in wrdLst:
        wrdLst.append(inpWord[i])
        

print(len(wrdLst)) 

  
Count=[] 

for i in range(len(wrdLst)):
    Cntr=0
    for j in range(len(inpWord)):
        if wrdLst[i]==inpWord[j]:
            Cntr=Cntr+1
            
    Count.append(Cntr)  
    
print(*Count)  

##############################################################################
############################ Another method ##################################

from collections import OrderedDict
words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1
   
print(len(words))
print(*words.values())  
      


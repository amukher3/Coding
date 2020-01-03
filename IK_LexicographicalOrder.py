# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:18:12 2020

@author: Abhishek Mukherjee
"""

#Lexicographic order
# N can be 10^5
#So, time complexity might matter!!

#
# Complete the solve function below.
#
def solve(arr):
    
    Words=list()
    for i in range(len(arr)):
        Words.append(arr[i].split())

    #Soreted words
    SortedWords=[]    
    from operator import itemgetter
    SortedWords=sorted(Words,key=itemgetter(0))    
    
    #list of the values
    Vals=[]
    Keys=[]
    for i  in range(len(Words)):
        Vals.append(SortedWords[i][1])
        Keys.append(SortedWords[i][0])
        
        #sorting the values 
        #of every key in lexicographic order
        KeyCounts=[]    
        tempKeys=[]

    for i in  range(len(Keys)):
            if Keys[i] not in tempKeys:
                tempKeys.append(Keys[i])
                KeyCounts.append(Keys.count(Keys[i]))

    stPos=0   
    tempVals=[] 
    FinalVals=[]
    for i in range(len(KeyCounts)):
        enPos=stPos+KeyCounts[i]
        FinalVals.append(sorted(Vals[stPos:enPos],reverse=True)[0])
        stPos=enPos
    
    FinalKeys=[]    
    for i in range(len(Keys)):
        if Keys[i] not in FinalKeys:
            FinalKeys.append(Keys[i])
        
    #Output format#
    opList=[]
    for i in range(len(FinalVals)):
        str_a="{0}:{1},{2}".format(FinalKeys[i],KeyCounts[i],FinalVals[i])
        opList.append(str_a)
        
    return opList
    


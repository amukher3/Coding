# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 02:34:41 2019

@author: Abhishek Mukherjee
"""
from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    numDivs=int(len(string)/k)
    stPos=0
    lst=[]
    for i in range(numDivs):
        enPos=k*(i+1)-1
        lst.append(string[stPos:enPos+1])
        print("".join(OrderedDict.fromkeys(lst[i])))
        stPos=enPos+1
        
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
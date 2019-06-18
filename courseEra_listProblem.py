# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 21:41:24 2019

@author: Abhishek Mukherjee
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list() 
for line in fh:                     
    word= line.split()    
    for element in word:              
        if element in lst:
            continue               # do nothing
        else :                     # else if element is not in the list
            lst.append(element)    # append     
lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print(lst)                          # print the list
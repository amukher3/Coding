# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:52:50 2019

@author: amukher3
"""


names=['jacob','Alex']

def likes(names):

    lst=names 


    if len(lst)==0:
        return 'no one likes this'
    elif len(lst)==1:
        return "%s likes this" %(lst[0])
    elif len(lst)==2:
        return "%s and %s like this" %(lst[0],lst[1])
    elif len(lst)==3:
        return "%s,%s and %s like this" %(lst[0],lst[1],lst[2])
    elif len(lst)>=4:
        temp= len(lst)-2
        return "%s, %s and %s others like this" %(lst[0],lst[1],temp)


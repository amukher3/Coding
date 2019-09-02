# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:39:48 2019

@author: amukher3
"""

def remove_smallest(numbers):
    
    a=numbers[:]
    
    if a ==[]:
        
        return a
    
    else:
        
        a.remove(min(a))
    
        return a
    
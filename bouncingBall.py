# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:26:24 2019

@author: amukher3
"""

def bouncingBall(h,bounce,WindowHeight):
    
    if h>0 and 0<bounce<1 and WindowHeight<h:
        
        
        
        
        i=1
        
        BounceHeight=bounce*h
        
        while BounceHeight>WindowHeight:
            
            i=i+2
            
            tempBounce=BounceHeight*bounce
            
            BounceHeight=tempBounce
    else:
        i=-1        
            
    return i
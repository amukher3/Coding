# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 05:03:47 2019

@author: Abhishek Mukherjee
"""

#Polar co-ordinates 

#import cmath.phase 
import cmath

lst = list(map(str, input().split("-")))
if len(lst)==1:
    lst=lst[0].split("+")
    ImPart=lst[1]
    ImNum=ImPart[:-1]
    RealPart=lst[0]
    print(abs(complex(int(RealPart), int(ImNum))))
    print(cmath.phase(complex(int(RealPart), int(ImNum))))
elif len(lst)==2:
    lst2=lst[1].split("+")
    if len(lst2)==2:
        ImPart=lst2[1]
        ImNum=ImPart[:-1]
        RealPart=lst2[0]
        print(abs(complex(-int(RealPart), int(ImNum))))
        print(cmath.phase(complex(-int(RealPart), int(ImNum))))   
    else:    
        ImPart=lst[1]
        ImNum=ImPart[:-1]
        RealPart=lst[0]
        print(abs(complex(int(RealPart), -int(ImNum))))
        print(cmath.phase(complex(int(RealPart), -int(ImNum))))    
elif len(lst)==3:
    ImPart=lst[2]
    ImNum=ImPart[:-1]
    RealPart=lst[1]
    print(abs(complex(-int(RealPart), -int(ImNum))))
    print(cmath.phase(complex(-int(RealPart), -int(ImNum))))    
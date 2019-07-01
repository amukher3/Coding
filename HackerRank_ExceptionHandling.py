# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:43:45 2019

@author: Abhishek Mukherjee
"""


# Number of test cases
T=list(map(int, input()))
a=[]
b=[]
for i in range(T[0])    :
    lst=list(map(str, input().split()))
    a.append(lst[0])
    b.append(lst[1])
    
for i in range(len(a)):
     if b[i]=='0':
         try:
            print(int(a[i])//int(b[i]))
         except ZeroDivisionError as e:
            print("Error Code:",e) 
     else:  
         try:
            print(int(a[i])//int(b[i]))
         except ValueError as e:
            print("Error Code:",e) 
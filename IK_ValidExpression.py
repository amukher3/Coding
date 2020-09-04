# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:30:11 2020

@author: Abhishek Mukherjee
"""

def is_valid(s):
    # Write your code here
    temp=[]
    flag=0
    c=0
    c1=0
    for cnt,i in enumerate(s):
        if i=='(' or i=='{' or i=='[':
            temp.append(i)
            c+=1
        elif i==')' or i=='}' or i==']':
            if cnt==0 or c==0:
                return 0
            else:
                if (temp[len(temp)-1]=='(' and i==')') or (temp[len(temp)-1]=='{' and i=='}') or (temp[len(temp)-1]=='[' and i==']'):
                    temp.pop()
        elif i.isdigit():
            if flag==0 and c1!=0:
                return 0
            else:
                flag=0
            c1+=1
        elif i=='+' or i=='-' or i=='*':
            if cnt==0 or flag==1:
                return 0
            else:
                if flag==1:
                    return 0
                else:
                    flag=1
        
    if temp==[] and flag==0:
        return 1
    else:
        return 0

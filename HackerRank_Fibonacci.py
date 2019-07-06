# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:27:41 2019

@author: Abhishek Mukherjee
"""

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):

        # return a list of fibonacci numbers
    x=list(range(0,n))
    
    if n==1:
        x[0]=0
        return [x[0]]
    elif n==2:
        x[1]=1
        return [x[0],x[1]]
    elif n>2:
        
        for n in range(n-2):
            x[n+2]=x[n]+x[n+1]
    return x    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
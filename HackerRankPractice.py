# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 03:19:39 2019

@author: Abhishek Mukherjee
"""

S='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
S='ABC'
n=2
numTimes=int(len(S)/n)
remLen=len(S)%n

for i in range(1,numTimes+2):
    if(i<=numTimes+1):
        print(S[(i-1)*n:(n-1)*i+1])
    else:
    
        print(S[-remLen:])
        
###############################################################
import textwrap
def wrap(string, max_width):
    import textwrap
     
    wrapper = textwrap.TextWrapper(width=max_width) 
  
    word_list = wrapper.fill(text=string) 
    return word_list


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
#######################################################################
import textwrap  
S='ABCDEFGHIJKLIMNOQRSTUVWXYZ'  
wrapper = textwrap.TextWrapper(width=4) 
  
word_list = wrapper.fill(text=S) 
  
# Print each line. 
for element in word_list: 
    print(element)     
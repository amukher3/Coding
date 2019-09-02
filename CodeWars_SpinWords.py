# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:15:53 2019

@author: amukher3
"""

def spin_words(sentence):
    # Your code goes here
    
    lst=sentence.split()
    for i in range(len(lst)):
        if len(lst[i])>=5:
            ReversedString=''.join(reversed(lst[i]))
            lst[i]=ReversedString
        
    
    
    str=' '.join(lst)
    return str
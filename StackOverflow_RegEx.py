# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:11:41 2020
@author: Abhishek Mukherjee

https://stackoverflow.com/questions/61624992/python-regexpt-to-match-a-word-with-several-dots

"""

import re
temp= re.split('\.',str1)     
temp2=[]        
[temp2.append(i) for i in temp if i.isalpha()]  

if ''.join(temp2)=='catfish':
    print('Match Found')
else:
    print('Doesn\'t Match')

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 01:28:34 2019

@author: Abhishek Mukherjee
"""

from itertools import product

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
c=list(product(lst1, lst2))
for i in range(len(c)):
    print(c[i],end=" ")
    
###############################################################################
if __name__ == '__main__':
        string = input()
        print(any(c.isalnum() for c in string))
        print(any(c.isalpha() for c in string))
        print(any(c.isdigit() for c in string))
        print(any(c.islower() for c in string))
        print(any(c.isupper() for c in string))   
#############################################################################

#tuples excercise
        
if __name__ == '__main__':
   n = int(input())
   integer_list = list(map(int, input().split()))
   tuple_list=tuple(integer_list)
   print(hash(tuple_list))    
############################################################################

#iter tools permutations 
   
from itertools import permutations
lst = list(map(str, input().split()))
n=lst[1]
lst2=sorted(list(permutations(lst[0], int(n))))
for i in range(len(lst2)):
    print("".join(lst2[i]))
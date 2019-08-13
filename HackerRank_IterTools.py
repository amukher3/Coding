# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from itertools import combinations_with_replacement

word,space,numComb = input().rpartition(' ')

numComb=int(numComb)

lst=list(combinations_with_replacement(sorted(word),numComb))

for i in range(len(lst)):
    print("".join(lst[i]))
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:14:54 2019

@author: Abhishek Mukherjee
"""

txt="I am lonely"
spec="sentence"
if spec=="word":
    txt=txt[::-1]
    print(txt)
if spec=="sentence":
    mylist=txt.split()
    revlist=mylist.reverse()
    myList=" ".join(mylist)
    print(myList)
    
# Change this line for a different result
dec = 2

print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")
print(dec,oct(dec),hex(dec),bin(dec))   

number=10
for n in range(number):
        octal=oct(n+1)
        hexa=hex(n+1)
        binary=bin(n+1)
        #print(n+1,octal[2:],hexa[2:],binary[2:])
        print(n+1,octal,hexa,binary)
        
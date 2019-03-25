# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:20:50 2019

@author: TongDist
"""

inp1=input()
inp2=input()
i_l1=inp1.split()
i_l2=inp2.split()
n=int(i_l1[0])
m=int(i_l1[1])
in_l=[]
for i in i_l2:
    in_l.append(int(i))

in_l.sort()
if n>=m:
    while in_l[-m]>=in_l[-1]/2:
    
        ma=in_l.pop()
        in_l.append(in_l[-1]/2)
        in_l.append(in_l[-1]/2)
        in_l.sort()
print(in_l[-m])

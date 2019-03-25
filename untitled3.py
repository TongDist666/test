# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:13:11 2019

@author: TongDist
"""

inp=input()
print(list(inp))
asd='asd'
try:
    
    print(inp)
    print(type(inp))
    inp_list=inp.split()
    print(inp_list)
    print(eval(inp))
    
    print(type(eval(inp)))
except:
    print('something wrong')
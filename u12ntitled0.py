# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:59:45 2019

@author: TongDist
"""
import numpy as np
a=12
b=34
c=complex(a,b)
print(c)
t=[]
t.append(c)
print(t)
t=np.mat(t)
#print(t.shape)

test=np.mat([[1,2],[3,4]])
test2=np.mat([1+1j])
print(test.shape)
print(test2.shape)
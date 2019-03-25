# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:58:15 2019

@author: TongDist
"""

s='CH4_p01_0chi423.271tf0300to0300Tst1625'
s_1=s.split('chi')[1].split('tf')
s_2=s_1[1].split('to')
s_3=s_2[1].split('Tst')
print(s_1[0])
print(s_2[0])
print(s_3[0])
print(s_3[1])
sss=-7e20
print(sss)
def w1():
   print('正在装饰')
   def inner():
        print('正在验证权限')
        return inner()
w1()

import numpy as np

t=np.array([[1,2,3],[5,6,7]],np.uint16)
print(t)
print(t[1,1])
print(t[1][1])
print(2^1^3^3)
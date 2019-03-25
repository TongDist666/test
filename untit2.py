# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:22:08 2019

@author: TongDist
比较   nonzero和自己写的函数的时间
"""

import numpy as np
import time


A = np.eye(10)
s1=time.time()
count=0
while count<1000:
    x = A.nonzero()
    result=[]
    for i in range(len(x[0])):
        result.append([x[0][i],x[1][i]])
    count+=1
print(time.time()-s1)

A2 = np.eye(10)
count2=0
s2=time.time()
while count2<1000:
    r2=[]
    for i in range(len(A2)):
        for j in range(len(A2[i])):
            if A2[i][j]!=0:
                r2.append([i,j])
    count2+=1
print(time.time()-s2)

ttt1=[[1,2,0,0,0,0,0,0,0,0,0,0,0,1,1,1],[1,2,0,0,0,0,0,0,0,0,0,0,0,1,1,1]]
#print(type(ttt1))
#获取矩阵中非零元素坐标
def get_nonzero(maxtrix):
    if isinstance(maxtrix,list):
        maxtrix = np.array(maxtrix) 
    x = maxtrix.nonzero()
    result=[]
    for i in range(len(x[0])):
        result.append([x[0][i],x[1][i]])
    return result
#print(get_nonzero(A))
print(get_nonzero(ttt1))

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:28:59 2019

@author: TongDist
"""

import matplotlib.pyplot as plt
import numpy as np

x= np.arange(-10, 10, 0.1)
y= np.arange(10, -10, -0.1)
#画线
plt.plot(x,y,'b-')
#plt.plot((3,3))
x1=[1,2,3]
y1=[3,2,1]
#plt.plot(x1,y1)
#画点
plt.plot(1,1,'b+')
plt.plot([1,2],[2,1],'r+')
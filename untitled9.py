# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:40:22 2019

@author: TongDist
"""

import cv2

img=cv2.imread('1.png')
#缩放时推荐使用 cv2.INTER_AREA，
#在扩展时推荐使用 v2.INTER_CUBIC（慢) 和 v2.INTER_LINEAR

#此处相对于 宽扩大2倍 高扩大2倍
kuo=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)

#等价于
#height,width=img.shape[:2]
#res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
while(1):
	#显示扩大后的图
    cv2.imshow('kuoda',kuo)
    #显示原图
    cv2.imshow('yuantu',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

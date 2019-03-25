# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:00:12 2019

@author: TongDist
"""

inp=input().split()
ip1=inp[0]
ip2=inp[1]
mask=inp[2]
ip1_l=ip1.split('.')
ip2_l=ip2.split('.')
mask_l=mask.split('.')
flag=0
count=0
result=''
for i in range(4):
    re1=int(ip1_l[i]) & int(mask_l[i])
    re2=int(ip2_l[i]) & int(mask_l[i])
    result+=str(re1)
    result+='.'
    if re1==re2:
        count+=1
    if re1==re2 and i==3 and count==4:
        flag=1
    
        

print(str(flag)+' '+result[:-1])
        
    

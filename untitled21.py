# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:33:13 2019

@author: TongDist
"""

def reshape(list_in,size=1):
    if len(list_in)%size!=0:
        print('input size is wrong!!')
        return False
    else:
        final_result,temp=[],[]
        for i in range(len(list_in)):
            if (i+1)%size!=0:
                temp.append(list_in[i])
            else:
                temp.append(list_in[i])
                final_result.append(temp)
                temp=[]
        return final_result
    
l=[1,2,3,4,5,6,1,2,3]
r=reshape(l,6)
print(r)
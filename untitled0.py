# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:19:40 2019

@author: TongDist
"""
inp1=input()
data_l=[]
for count in range(int(inp1)):
    data_l.append(input())

def g(sr):
    
    inp_l=list(sr)
    if len(sr)<3:
        return sr
    else:
        i=0
        while i<len(sr)-2:
#            print(i)
#            print(inp_l)
            if inp_l[i]==inp_l[i+1] and inp_l[i]==inp_l[i+2]:
                inp_l.pop(i+2)
                if len(inp_l[i:])>2 and inp_l[i]==inp_l[i+2]:
                    continue
            i+=1
            
            
        j=0
        while j<len(inp_l)-3:
            if inp_l[j]==inp_l[j+1] and inp_l[j+2]==inp_l[j+3]:
                inp_l.pop(j+3)
            if len(inp_l[j:])>3 and inp_l[j+2]==inp_l[j+3]:
                continue
            
            j+=1
        result=''
        for dl in inp_l:
            result+=dl
        return result
for d in data_l:
   print(g(d))
#while i<len(inp)-2:
#    if inp[i]==inp[i+1] and inp[i]==inp[i+2]:
#        inp=inp[:i+2]+inp[i+2:]
#        #if inp[]
#if len(inp)>3:
#    for j in range(len(inp)-3):
#        if inp[i]==inp[i+1] and inp[i+2]==inp[i+3]:
#            inp=inp[:i+2]+inp[i+3:]
#            print(inp)
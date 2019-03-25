# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:53:10 2019

@author: TongDist
"""

s='1235asdf'
#print('as' in s)
#print(s.split('1235'))
#print(''.join(ss for ss in s.split('1235')))

def wordBreak(s, wordDict):
        for i in wordDict:
            
            if i in s:
                s_temp=s.split(i)
                print(s_temp)
                s=''.join(st for st in s_temp)
                print(s)
            if not s:
                return True
        if s:
           return False
       
t1="leetcode"
t2=["leet","code"]
print(wordBreak(t1,t2))

import numpy as np
ff=np.mat([[1,2,3],[4,5,6]])
ff2=np.mat([[1,2,3],[4,5,6]])
print(ff[1,])
print(ff+ff2)

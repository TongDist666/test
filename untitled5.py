# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:58:53 2019

@author: TongDist
"""

def search_m(matrix):
    m=len(matrix)
    if m==0:
        return 0
    n=len(matrix)
    if n==0:
        return 0
    res=0
    dp=[[0 for i in range(n)] for j in range(m)]
    for i in range(0,m):
        if matrix[i][0]=='1':
            dp[i][0]=1
            res=1
    for j in range(0,n):
        if matrix[0][j]=='1':
            dp[0][j]=1
            res=1
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j]=='1':
                dp[i][j]=matrix[i][j]=min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1
            res=max(res,dp[i][j])
    return res*res
inp=input()
l=[]
for i in range(int(inp)):
    temp=input()
    l.append(list(temp))
print(search_m(l))
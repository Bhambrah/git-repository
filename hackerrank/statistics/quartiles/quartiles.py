# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:05:33 2018

@author: Sumeet Bhambrah

Hackerrank | Statistics
Day 1: Quartiles

"""

n = int(input())
X = list(map(int, input().split()))
X.sort()
def median(arr):
    l = len(arr)-1
    m = l//2
    return(round((arr[m] if (l+1)%2!=0 else (arr[m]+arr[m+1])/2)))
q2 = median(X)
m = (n-1)//2
if(n%2==0):
    q1 = median(X[:m+1])
    q3 = median(X[m+1:])
else:
    q1 = median(X[:m])
    q3 = median(X[m+1:])
print(q1,q2,q3,sep='\n')
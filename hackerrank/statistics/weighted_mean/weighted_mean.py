# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:03:51 2018

@author: Sumeet Bhambrah

Hackerrank | 10 days of Statistics
Day 0: Weighted Mean

"""

n = int(input())
X = list(map(int,input().split()))
W = list(map(int,input().split()))
weighted_mean = sum(list(map(lambda x,y: x*y, X, W)))/sum(W)
print(round(weighted_mean,1))
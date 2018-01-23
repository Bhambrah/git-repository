# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:31:50 2018

@author: Sumeet Bhambrah

Hackerrank | 10 days of Statistics
Day 0 : Mean, Median, Mode

"""

n = int(input())
arr = map(int,input().split())
arr = list(arr)
mean = sum(arr)/n
arr.sort()

m = int((n-1)//2)
median = arr[m] if n%2 != 0 else ((arr[m]+arr[m+1])/2)

modal_dict = {}
for i in arr:
    modal_dict[i] = modal_dict.get(i,0) + 1
modes = [m for m in modal_dict.keys() if modal_dict[m]==max(modal_dict.values())]
mode = min(modes)

print("%.1f \n%.1f \n%d" % (mean,median,mode))
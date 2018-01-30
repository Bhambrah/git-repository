# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:21:16 2018

@author: Sumeet Bhambrah

Hackerrank | Python | Collections |company logo

"""


'''
# without using collections

from itertools import groupby

s = input()
count = {}
for c in s:
    count[c] = count.get(c, 0) + 1

result=[]
temp = list(count.items())
temp.sort(key=lambda x:x[1], reverse=True)
for key, group in groupby(temp, lambda x:x[1]):
    result = result + sorted(list(group))
    if(len(result)>=3):
        break

for ch,c in result[:3]:
    print(ch,c)
'''


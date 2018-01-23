# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:51:55 2018

@author: Sumeet Bhambrah

Hackerrank | Python | Iterables | Iterables and Iterators

"""
import itertools

n = int(input())
letters = input().split()
k = int(input())

count = 0
combinations = list(itertools.combinations(letters, k))
for elem in combinations:
    if 'a' in elem:
        count+=1
probability = count/len(combinations)
print("%0.3f" % probability)
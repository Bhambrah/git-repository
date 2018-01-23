# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:24:48 2018

@author: Sumeet Bhambrah

Hackerrank | Python | Itertools | Compress the String

"""
from itertools import groupby

s = input()
result = ""
for key, group in groupby(s):
    result = result + "({},{}) ".format(len(list(group)), key)
print(result)
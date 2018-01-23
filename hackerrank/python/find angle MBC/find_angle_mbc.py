# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:10:52 2018

@author: Sumeet Bhambrah

Hackerrank | Python | Math | Find angle MBC

"""

import math

ab = int(input())
bc = int(input())

p = ab/2
b = bc/2

mbc = math.atan(p/b)
mbc = math.degrees(mbc)
print(str(round(mbc))+'°')
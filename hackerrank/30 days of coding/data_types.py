# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:35:18 2018

@author: Sumeet Bhambrah

Hackerrank | 30 days of coding | data types

"""

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
ii = 1
dd = 1.0
ss = ""
# Read and save an integer, double, and String to your variables.
ii = int(input())
dd = float(input())
ss = input()
# Print the sum of both integer variables on a new line.
print("%d" % (i + ii))
# Print the sum of the double variables on a new line.
print("%.1f" % (d + dd))
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + ss)

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:06:26 2018

@author: Sumeet Bhambrah

Permutations of string

BackTracking
"""

def permuteHelper(string, chosen):
    for i in range(len(chosen)):print(" ", end="")
    print("permuteHelper({}, {})".format(string, chosen))
    if(string == ""):
        print("".join(chosen))
    else:
        for i in range(len(string)):
            chosen.append(string[i])
            string = string[:i] + string[i+1:]
            permuteHelper(string, chosen)
            ch = chosen.pop()
            string = string[:i] + ch + string[i:]

def permute(string):
    permuteHelper(string, [])
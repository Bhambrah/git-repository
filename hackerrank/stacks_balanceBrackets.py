# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:01:50 2018

@author: Sumeet Bhambrah

Hackerrank | Cracking the Coding Interview

Stacks: Balanced Brackets

"""

def is_matched(expression):
    a = []
    end = {'(':')', '{':'}', '[':']'}
    for char in expression.strip():
        if char in ('(', '{', '['):
            a.append(char)
        else:
            if(a==[]):
                return False
            else:
                if(char != end[a[-1]]):
                    return False
                else:
                    a.pop()
    return True if a == [] else False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

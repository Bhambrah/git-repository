# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:15:28 2018

@author: Sumeet Bhambrah

Hackerrank | Cracking the Coding Interview

Strings: Making Anagrams

Alice is taking a cryptography class and finding anagrams to be very useful.
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string.
In other words, both strings must contain the same exact letters in the same exact frequency.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the 
minimum number of character deletions required to make the two strings anagrams. 
Can you help her find this number? 
Given two strings, a and b, that may or may not be of the same length,
determine the minimum number of character deletions required to make a and b anagrams.
Any characters can be deleted from either of the strings. 

Input Format
The first line contains a single string, a.
The second line contains a single string, b.

Constraints
1<=|a|, |b|<=10^4
It is guaranteed that a and b consist of lowercase English alphabetic letters (i.e., a through z).

Output Format
Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

"""

def number_needed(a, b):
    A = list(a)
    B = list(b)
    for i in a:
        if i in B:
            A.remove(i)
            B.remove(i)
    return(len(A)+len(B))
a = input().strip()
b = input().strip()

print(number_needed(a, b))

'''
The first solution above has O(n^2) time complexity.
Can be tried for more optimmized solution?

'''
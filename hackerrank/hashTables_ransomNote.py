# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:24:38 2018

@author: Sumeet Bhambrah

Hackerrank | Cracking the Coding Interview

Hash tables: Ransom Note

A kidnapper wrote a ransom note but is worried it will be traced back to him.
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note.
The words in his note are case-sensitive and he must use whole words available in the magazine, 
meaning he cannot use substrings or concatenation to create the words he needs.
Given the words in the magazine and the words in the ransom note,
print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Input Format
The first line contains two space-separated integers describing the respective values of 
(the number of words in the magazine) and (the number of words in the ransom note). 
The second line contains space-separated strings denoting the words present in the magazine. 
The third line contains space-separated strings denoting the words present in the ransom note.

Constraints.

1<=m,n<=30000
1<=len(any word)<=5
Each word consists of English alphabetic letters (i.e., a to z and A to Z).
The words in the note and magazine are case-sensitive.

Output Format
Print Yes if he can use the magazine to create an untraceable replica of his ransom note; otherwise, print No.

"""

def ransom_note(magazine, ransom):
    mag_dict = {}
    for word in magazine:
        mag_dict[word] = mag_dict.get(word, 0) + 1
    for word in ransom:
        if(mag_dict[word] == 0):
            return 0
        else:
            mag_dict[word] = mag_dict[word] - 1
    return 1

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer and not(m<n)):
    print("Yes")
else:
    print("No")
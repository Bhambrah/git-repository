# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:25:58 2018

@author: Sumeet Bhambrah

Hackerrank | Python | Sets | No Idea

There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B.
Your initial happiness is 0. For each i integer in the array, if i belongs to A, you add 1 to your happiness.
If i belongs to B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end. 
Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements. 

Constraints 
1<=n<=10^5
1<=m<=10^5
1<=input number<=10^9

Input Format
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array. 
The third and fourth lines contain m integers, A and B, respectively.

Output Format
Output a single integer, your total happiness.

"""

(n,m) = input().split()
array = input().strip().split()
A = {i for i in input().strip().split()}
B = {i for i in input().strip().split()}

happiness = 0
count = {}
for i in array:
    count[i] = count.get(i, 0) + 1
for i in A & set(array):
    happiness += 1 * count[i]
for i in B & set(array):
    happiness += (-1) * count[i]
print(happiness)
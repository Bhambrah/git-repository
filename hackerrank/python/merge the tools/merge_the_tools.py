# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:07:28 2018

@author: Sumeet Bhambrah

Hackerrank | Python | Strings | Merge the Tools!

Consider the following:
A string, s, of length n, where s=c[0]c[1]...c[n-1]
An integer, k, where k is a factor of n.
We can split s into n/k subsegments where each subsegment, t[i], consists of a contiguous block of k characters in s.
Then, use each t[i] to create string u[i] such that:
The characters in u[i] are a subsequence of the characters in t[i].
Any repeat occurrence of a character is removed from the string such that each character in u[i]
occurs exactly once. In other words, if the character at some index j in t[i] occurs at a previous index < j in t[i],
then do not include the character in string.
Given s and k, print n/k lines where each line i denotes string u[i].

Input Format
The first line contains a single string denoting s. 
The second line contains an integer, k, denoting the length of each subsegment.

Constraints:
1<=n<=10^4, where n is the length of s
1<=k<=n
It is guaranteed that n is a multiple of k
. 
Output Format
Print n/k lines where each line i contains string u[i].
"""

def merge_the_tools(string, k):
    u = []
    for i in range(1,len(string)+1,k):
        word = ''
        count = {}
        for j in range(i,i+k):
            count[string[j-1]] = count.get(string[j-1], 0)+1
            if(count[string[j-1]] == 1):
                word = word + string[j-1]
            else:
                continue
        u.append(word)
    for t in u:
        print(t)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:49:14 2018

@author: Sumeet Bhambrah

Hackerrank | Cracking the Coding Interview

Arrays: Left Rotation

A left rotation operation on an array of size shifts each of the array's elements unit to the left.

Given an array of integers and a number, perform left rotations on the array.
Then print the updated array as a single line of space-separated integers.

Input Format
The first line contains two space-separated integers denoting the respective values of 
(the number of integers) and (the number of left rotations you must perform). 
The second line contains space-separated integers describing the respective elements of the array's initial state.

Constraints
1<=n<=10^5
1<=d<=n
1<=a[i]<=10^6

Output Format
Print a single line of space-separated integers denoting the final state of the array after performing left rotations.

"""

def array_left_rotation(a, n, k):
    f = [0]*n
    for i in range(n):
        j = (i-k)%n
        f[j] = a[i]
    return(f)    

n, k = map(int, input("Enter space separated values for size of array and number of left rotations to be performed: ").strip().split(' '))
a = list(map(int, input("Enter space separated values for array elements: ").strip().split(' ')))
answer = array_left_rotation(a, n, k);
print("Final array after {} left rotations \n on {} \n is {}.".format(k,a,answer))
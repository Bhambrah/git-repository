# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:24:31 2018

@author: Sumeet Bhambrah

Maximum Sum Subarray with Sum less than or equal to a given number

"""

def maxSum_subarray (array, s):
    cur_sum = 0
    max_sum = 0
    start = 0
    for i in range(len(array)):
        cur_sum += array[i]
        while(cur_sum > s and start<i):
            cur_sum -= array[start]
            start+=1
        if(i==0 or (cur_sum <= s and max_sum < cur_sum)):
            max_sum = cur_sum
            p = start
            q = i+1
        # print(array[p:q],max_sum)
    return(array[p:q], max_sum)

array = list(map(int, input("Enter space separated numbers for the array: ").split()))
s = int(input("Enter given sum: "))

sub, max_sum = maxSum_subarray(array,s)
print("Maximum sum subarray with sum less than or equal to {} is {} (subarray sum = {})".format(s,sub,max_sum))
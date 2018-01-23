# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 22:37:26 2018

@author: Sumeet Bhambrah

Hackerrank | Cracking the Coding Interview

Linked Lists: Detect a cycle
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. 
Complete the function provided in the editor below.
It has one parameter: a pointer to a Node object named head that points to the head of a linked list.
Your function must return a boolean denoting whether or not there is a cycle in the list.
If there is a cycle, return true; otherwise, return false.
Note: If the list is empty, head will be null.
Input Format
Our hidden code checker passes the appropriate argument to your function. You are not responsible for reading any input from stdin.

Constraints
0<=list size<=100

Output Format
If the list contains a cycle, your function must return true. If the list does not contain a cycle, it must return false.
The binary integer corresponding to the boolean value returned by your function is printed to stdout by our hidden code checker.
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

"""

''' Note: Run the function code below in the Hackerrank console:
    https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem '''

def has_cycle(head):
    if(head):
        prev = {}
        current = head
        if(current.next == None):
            return False
        while(current):
            if current.next in prev:
                return True
            else:
                prev[current] = 1
                current = current.next
        return(False)
    return(False)
    
    

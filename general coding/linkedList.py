# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:34:34 2018

@author: Sumeet Bhambrah
"""

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
    
class LinkedList():
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def addAt0(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp
    def deleteAt0(self):
        if(self.head == None):
            print("Nothing to delete")
        else:
            temp = self.head
            self.head = self.head.getNext()
            temp.setNext(None)
            del(temp)
            print("Node 0 deleted")
    def display(self):
        current = self.head
        while(current):
            print(current.getData(), end=" -> ")
            current = current.getNext()
        print("None")
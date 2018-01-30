# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:57:09 2018

@author: Sumeet Bhambrah

Binary search tree


"""

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l is not None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r is not None):
                self._add(val, node.r)
            else:
                node.r = Node(val)
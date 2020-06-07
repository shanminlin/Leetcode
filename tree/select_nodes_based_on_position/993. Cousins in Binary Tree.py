#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# 
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# 
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
# 
# Return true if and only if the nodes corresponding to the values x and y are cousins.
# 
# Note:
# 
# The number of nodes in the tree will be between 2 and 100.<br>
# Each node has a unique integer value from 1 to 100.
# <img src='../images/cousin.png'>
#  

# # Brainstorm
# 
# Traverse the tree, we need to keep track the level of each node, and its parent node.

# In[ ]:





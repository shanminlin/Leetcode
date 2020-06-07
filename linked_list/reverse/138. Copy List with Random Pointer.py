#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
# 
# val: an integer representing Node.val<br>
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
#  
# 
# Constraints:
# 
# -10000 <= Node.val <= 10000<br>
# Node.random is null or pointing to a node in the linked list.<br>
# Number of Nodes will not exceed 1000.

# # Brainstorm
# 
# With random pointers, if the random node already exists, we need to create a pointer to that existing node. If the random node does not exist, we need to create a new node, but for some next nodes along the linked list, we need to remember to point to that already exist random node, not creating a new one.<br>
# 
# So we have to keep track of the nodes we have created. If any next or random node already exists, we don't create new nodes.

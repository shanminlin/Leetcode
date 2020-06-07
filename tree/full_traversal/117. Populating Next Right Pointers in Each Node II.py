#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a binary tree
# 
# struct Node {<br>
#   int val;<br>
#   Node *left;<br>
#   Node *right;<br>
#   Node *next;<br>
# }<br>
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
#  
# 
# Follow up:
# 
# You may only use constant extra space.<br>
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
#  
# Constraints:
# 
# The number of nodes in the given tree is less than 6000.<br>
# -100 <= node.val <= 100

# # Brainstorm
# 
# - queue to process nodes and keep track of the number of nodes in each level
# - pop the front of the queue, its next pointer is the front of the current queue.

# # Solution

# In[ ]:


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        queue = deque([root])
        while queue:
            num_of_nodes = len(queue)
            for i in range(num_of_nodes):
                node = queue.popleft()
                if i == num_of_nodes - 1:
                    node.next = None
                else:
                    node.next = queue[0]
                    
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        
        return root


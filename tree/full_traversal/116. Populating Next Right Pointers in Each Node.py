#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
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
# The number of nodes in the given tree is less than 4096.<br>
# -1000 <= node.val <= 1000<br>

# # Solution
# Time O(N), Space O(1)

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

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        
        
        leftmost = root
        head = leftmost
        # If no leftmost.left, meaning we have done the last level
        while leftmost.left:
            
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left

                head = head.next
            
            leftmost = leftmost.left
            head = leftmost
            
        return root


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# <img src='./images/LCD.png'>

# # Brainstorm 
# 
# This question is not trivial.
# 

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        elif root == p or root == q:
            return root
  
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
         
        else:
            return left or right # what about the case when both left and right are None?


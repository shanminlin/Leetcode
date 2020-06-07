#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# <img src='../images/flatten.png'>

# # Brainstorm
# 
# The recursive relation is not easy to find.
# If we flatten a simple left subtree 2->3->4, we need to reach the end of it to attach the flattend right subtree.
# - Time O(N^2), space O(N) depending on the height of the tree, typical DFS.
# 
# How can we remove the while loop to reach the bottom of the left tree to reduce time?
# - Attach right tree to the bottom right of the left tree.
# - after all right tree is None, attache left to right.

# # Solution 1
# ##### left subtree then right subtree

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return 
        
        self.flatten(root.left)
        self.flatten(root.right)
            
        
        if root.left:
            right = root.right
            root.right = root.left
            root.left = None
            
            # Find the bottom node of left tree
            node = root.right
            while node.right:
                node = node.right
            node.right = right


# # Solution 2
# ##### right subtree then left subtree

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return 
        
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        if root.left:
            node = root.left
            while node.right:
                node = node.right
            node.right = root.right
            
            root.right = root.left
            root.left = None


# # Solution 3
# ##### No while loop

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        return self.helper(root, None)
    
    def helper(self, root, prev):
        
        if root is None:
            return prev
        
            
        prev = self.helper(root.right, prev)
        prev = self.helper(root.left, prev)
        
        root.right = prev
        root.left = None
        prev = root
        return prev


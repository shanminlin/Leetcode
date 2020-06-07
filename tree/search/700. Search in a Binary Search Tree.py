#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

# # Brainstorm
# 
# DFS to search based on left and right subtree

# # Solution 1
# ##### DFS

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return []
        
        return self.dfs(root, val)
    
    def dfs(self, root, val):
        if root is None:
            return 
        
        if root.val > val:
            return self.dfs(root.left, val)  # Don't forget return
            
        elif root.val < val:
            return self.dfs(root.right, val)
        
        else:
            return root
        


# # Solution 2
# 

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root
        
        return None


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
# 
# Assume a BST is defined as follows:<br>
# 
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.<br>
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.<br>
# Both the left and right subtrees must also be binary search trees.<br>
#  
# 
# For example:<br>
# Given BST [1,null,2,2],<br>
# return [2].<br>
# 
# Note: If a tree has more than one mode, you can return them in any order.<br>
# 
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

# # Brainstorm
# 
# 

# # Solution 1
# ##### not making use of BST property

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def dfs(self, root, count):
        if root is None:
            return 
        
        count[root.val] += 1
        self.dfs(root.left, count)
        self.dfs(root.right, count)
        
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        count = defaultdict(int)
        
        self.dfs(root, count)
        
        mode = []
        max_value = max(count.values())
            
        for key, value in count.items():
            if value == max_value:
                mode.append(key)
                
        return mode


# # Solution 2
# ##### 

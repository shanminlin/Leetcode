#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# 
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
# 
# Example 1:
# 
# <img src='../images/merge_two_trees.png'>
#  
# 
# Note: The merging process must start from the root nodes of both trees.

# # Brainstorm
# 
# Traverse both trees, if the nodes at a particular position in both trees are present, update t1's value.
# What if a node is missing in one tree?
# - t1.left = mergeTrees(t1.left, t2.left)
# 

# # Solution 1
# ##### BFS

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        
        stack = []
        stack.append([t1, t2])
        while stack:
            t = stack.pop()
            if t[0] is None or t[1] is None:
                continue
            t[0].val += t[1].val
            
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append([t[0].left, t[1].left])
                
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append([t[0].right, t[1].right])
                
        return t1


# # Solution 2
# ##### DFS

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return
        elif t1 and t2:
            t1.val += t2.val
        else:
            return t1 or t2
        
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1


# My wrong solution:
# forgot to return recursive function

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return
        elif not t1:
            t1 = t2
        elif t1 and t2:
            t1.val += t2.val
            
        self.mergeTrees(t1.left, t2.left)
        self.mergeTrees(t1.right, t2.right)
        
        return t1


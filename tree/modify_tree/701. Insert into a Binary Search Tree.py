#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# 
# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
# 
# Constraints:
# 
# The number of nodes in the given tree will be between 0 and 10^4.<br>
# Each node will have a unique integer value from 0 to -10^8, inclusive.<br>
# -10^8 <= val <= 10^8<br>
# It's guaranteed that val does not exist in the original BST.<br>

# # Brainstorm
# 
# Compare with root, go to left or right subtree. Compare with the root, go to left or right subtree.

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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        
        if root.right is None and val > root.val:
            root.right = TreeNode(val)
        elif root.left is None and val < root.val:
            root.left = TreeNode(val)
            
        
        if val > root.val:
            self.insertIntoBST(root.right, val)
        else:
            self.insertIntoBST(root.left, val)
            
        return root


# # Solution 2
# ##### DFS, simplified

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
            
        return root
            


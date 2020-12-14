#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# 
# Note:
# - You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# Follow up:
# - What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# # Brainstorm
# 
# 

# # Solution

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return
        
        # in order traversal
        output = self.inorder_traversal([], root)
        return output[k-1]
        
    def inorder_traversal(self, output, root):
        if root is None:
            return 

        self.inorder_traversal(output, root.left)
        output.append(root.val)
        self.inorder_traversal(output, root.right)
                
        return output


# In[ ]:





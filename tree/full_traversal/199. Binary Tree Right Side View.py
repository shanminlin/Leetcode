#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# # Solution

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        
        result = []
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue) 
            for i in range(num_nodes):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                
                if i == num_nodes - 1:
                    result.append(node.val)
                    
        return result


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Find the sum of all left leaves in a given binary tree.

# # Brainstorm
# 
# As we need to traverse every node to get the answer, we can use both BFS and DFS with the same time complexity O(N).

# # Solution 1
# ##### BFS

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        
        sum_left = 0
        
        queue = deque([(root, False)])
        while queue:
            
            node, is_left = queue.popleft()
            
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
                
            
            if is_left and node.left is None and node.right is None:
                sum_left += node.val
                
        return sum_left
            


# # Solution 2
# ##### DFS

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.sum_left = 0
        is_left = False
        self.dfs(root, is_left)
        return self.sum_left
    
    def dfs(self, root, is_left):
        if root is None:
            return
        
        if is_left and root.left is None and root.right is None:
            self.sum_left += root.val
            
        self.dfs(root.left, True)
        self.dfs(root.right, False)


# # Solution 3
# ##### DFS, no global variable

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        is_left = False
        return self.dfs(root, is_left)
    
    def dfs(self, root, is_left):
        if root is None:
            return 0
        
        if is_left and root.left is None and root.right is None:
            return root.val
        elif not is_left and root.left is None and root.right is None:
            return 0
            
        return self.dfs(root.left, True) + self.dfs(root.right, False)


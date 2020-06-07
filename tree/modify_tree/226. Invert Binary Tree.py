#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# <img src='../images/invert_tree.png'>

# # Solution 1
# ##### BFS
# - BFS to visit the nodes, and at every node you are swapping its left and right subtrees. 
# - from top to bottom

# In[ ]:


from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
                
            if curr.right:
                queue.append(curr.right)
        
        return root


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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root


# # Solution 3
# ##### DFS, implement stack

# In[ ]:


def invertTree(self, root: TreeNode) -> TreeNode:
    if root is None:
        return None

    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root


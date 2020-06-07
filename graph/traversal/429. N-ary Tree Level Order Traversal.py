#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an n-ary tree, return the level order traversal of its nodes' values.
# 
# <img src='./images/nry.png'>
# 
# Constraints:
# 
# The height of the n-ary tree is less than or equal to 1000<br>
# The total number of nodes is between [0, 10^4]

# In[1]:


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# # Brainstorm
# 
# BFS (queue)

# # Solution 1
# ##### BFS

# In[ ]:


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        traversal = []
        queue = deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
            
                queue.extend(node.children)
                
            traversal.append(level)
            
        return traversal
        


# # Solution 2
# ##### DFS

# In[ ]:


# What is wrong with the following solution?

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        traversal = [[root.val]]
        level = []
        index = 0
        return self.dfs(root, level, index, traversal)
    
    def dfs(self, root, level, index, traversal):
        
        if root.children is None:
            return
        
        
        if index == 0:
            level = []
            traversal.append(level)
        
        for i, child in enumerate(root.children):
            level.append(child.val)
            self.dfs(child, level, i, traversal)
        
        return traversal


# In[17]:


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        traversal = []
        level = 0
        return self.dfs(root, level, traversal)
    
    def dfs(self, root, level, traversal):
        
        if root is None:
            return
        
        
        if len(traversal) == level:
            traversal.append([])
            
        traversal[level].append(root.val)
        
        for child in root.children:
            self.dfs(child, level+1, traversal)
        
        return traversal
        


# In[18]:


a.append([])


# In[19]:


a


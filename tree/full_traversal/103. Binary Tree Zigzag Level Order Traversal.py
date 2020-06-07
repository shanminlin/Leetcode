#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# 
# <img src='../images/zigzag.png'>

# # Solution 1
# ##### BFS
# - time O(N), space O(N)

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        all_nodes = []
        queue = deque([root])
        is_reverse = False
        while queue:
            level = deque()
            length = len(queue)
            
            for _ in range(length):
                node = queue.popleft()
                
                if not is_reverse:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            all_nodes.append(level)
            is_reverse = not is_reverse
            
        return all_nodes


# # Solution 2
# ##### DFS
# - time O(N), space O(N) for skewed tree, (average O(logN))

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        level = 0
        self.dfs(root, level, result)
        return result
    
    def dfs(self, root, level, result):
        if root is None:
            return
        
        if level == len(result):
            result.append(deque([root.val]))
            
        else:
            if level % 2 == 1:
                result[level].appendleft(root.val)
            else:
                result[level].append(root.val)
        
        self.dfs(root.left, level+1, result)
        self.dfs(root.right, level+1, result)


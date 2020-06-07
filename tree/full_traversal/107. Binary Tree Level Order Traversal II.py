#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        result = deque()
        queue = deque([root])
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                
            result.appendleft(level)
            
        return result


# # Solution 2
# ##### DFS

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = deque()
        level = 0
        self.dfs(root, level, result)
        return result
    
    def dfs(self, root, level, result):
        if root is None:
            return
        
        if level == len(result):
            result.appendleft([root.val])
        else:
            # Note the index is reversed
            result[-(level+1)].append(root.val)
            
        self.dfs(root.left, level+1, result)
        self.dfs(root.right, level+1, result)


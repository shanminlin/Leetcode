#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# <img src='../images/max_depth.png'>

# # Brainstorm
# 
# We need to keep track of the number of levels as we traverse the tree.
# The space complexity for DFS should be the tree's height, while the BFS is the num of nodes in the longest layer.So it depends on the shape of the tree and preference between recursion or iteration.
# For example, for DFS, where h is the height of the tree. If the tree is balanced, that's O(log n), if the tree is skewed, it's O(n). For BFS, for balancde tree, it's O(N/2). For skewed tree, it is O(1).
# 
# - BFS or DFS
#      - BFS search by layers so the number of layers is the depth
#      - DFS search by subtree so take longer to find the max depth subtree
#      - the above only applies to graph, for binary tree, the depth first search also have only two choices.
# - how to keep track of the number of layers?
#      - when you add a child, add a layer
# - runtime analysis
#      - iterate once, O(N) time
#      - use a stack, O(N) space

# # Solution 1
# ##### BFS and number of pops

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        num_level = 0
        
        while queue:
            num_level += 1
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return num_level


# # Solution 2
# ##### DFS, height

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root is None:
            return 0
        
        left = 1 + self.dfs(root.left)
        right = 1 + self.dfs(root.right)
        
        return max(left, right)
        
    def maxDepth(self, root: TreeNode) -> int:
        
        return self.dfs(root)


# # Solution 3
# ##### DFS, depth

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, depth):
        
        if root is None:
            return 0
        
        self.max_depth = max(depth, self.max_depth)
        
        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)
        
    def maxDepth(self, root: TreeNode) -> int:
        self.max_depth = 0
        self.dfs(root, 1)
        return self.max_depth


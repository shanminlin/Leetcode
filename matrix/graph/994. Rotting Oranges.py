#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# In a given grid, each cell can have one of three values:
# 
# the value 0 representing an empty cell;<br>
# the value 1 representing a fresh orange;<br>
# the value 2 representing a rotten orange.<br>
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.<br>
# 
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
# 
#  

# # Solution
# ##### BFS

# In[19]:


from collections import deque

class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return 0
        
        # Find location of rotten oranges as starting nodes
        # Count the number of fresh oranges to compare at the end
        queue = deque()
        fresh_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # Edge case
        if fresh_count == 0:
            return 0
        
        # BFS, modify entry of 1 if it is neighbor of 2
        layer = 0
        while queue:
            length = len(queue)
            
            # Pop the original layer
            for _ in range(length):
                i, j = queue.popleft()
                
                # Rotten its fresh neighbors
                neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for x, y in neighbors:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        
                        fresh_count -= 1
                        
                        # Append its rotten neighbors 
                        queue.append((x, y))
            
            # Move to next layer
            layer += 1
            
        if fresh_count == 0:
            return layer - 1
        else:
            return -1


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)<br>
# 
# Example 1:<br>
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],<br>
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],<br>
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],<br>
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],<br>
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],<br>
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],<br>
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],<br>
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]<br>
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# 
# Example 2:<br>
# [[0,0,0,0,0,0,0,0]]<br>
# Given the above grid, return 0.<br>
# Note: The length of each dimension in the given grid does not exceed 50.

# # Solution
# ##### DFS

# In[ ]:


class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        visited = set()
        max_area = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = self.dfs(i, j, visited, grid)
                    max_area = max(max_area, area)
                    
        return max_area
        
    def dfs(self, i, j, visited, grid):
        
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0 or (i, j) in visited:
            return 0
        
        visited.add((i, j))
        
        up = self.dfs(i-1, j, visited, grid)
        down = self.dfs(i+1, j, visited, grid)
        left = self.dfs(i, j-1, visited, grid)
        right = self.dfs(i, j+1, visited, grid)
        
        return 1 + up + down + left + right


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# 
# Example 1:<br>
# Input:<br>
# 11110<br>
# 11010<br>
# 11000<br>
# 00000<br>
# 
# Output: 1<br>
# 
# Example 2:<br>
# Input:<br>
# 11000<br>
# 11000<br>
# 00100<br>
# 00011<br>
# 
# Output: 3

# # Brainstorm
# 
# - Traverse the matrix. If the element has value 1, continue traversing in 4 directions and mark all elements with 1 in the path so that each element is visited only once.
# - To keep track of visited elements with value 1, we have two options:
#      - use a visited set: more space
#      - modify the cell value to something like # or 0: less space but destroys the original matrix.
# 
# 

# # Solution 1
# ##### BFS

# This solution exceeds time limit.

# In[ ]:


from collections import deque
class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        island_count = 0
        queue = deque()
        visited = set()
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1' and (i, j) not in visited:
                    island_count += 1
                    queue.append((i, j))
                    
                while queue:
                    x, y = queue.popleft()
                    visited.add((x, y))
                    # check and append children to queue 
                    if x > 0:
                        if grid[x-1][y] == '1' and (x-1, y) not in visited:
                            queue.append((x-1, y))
                    if y > 0:
                        if grid[x][y-1] == '1' and (x, y-1) not in visited:
                            queue.append((x, y-1))
                    if x < nrow - 1:
                        if grid[x+1][y] == '1' and (x+1, y) not in visited:
                            queue.append((x+1, y))
                    if y < ncol - 1:
                        if grid[x][y+1] == '1' and (x, y+1) not in visited:
                            queue.append((x, y+1))
                            
        return island_count


# # Solution 2
# #### DFS with visited set

# In[ ]:


# DFS
def numIslands(grid):
    if grid is None or len(grid) == 0:
        return 0

    nrow = len(grid)
    ncol = len(grid[0])
    num_islands = 0
    
    for row in range(nrow):
        for col in range(ncol):
            if grid[row][col] == '1':
                num_islands += 1
                dfs(grid, row, col)


    return num_islands

def dfs(grid, row, col):
    nrow = len(grid)
    ncol = len(grid[0])

    if row < 0 or col < 0 or row >= nrow or col >= ncol or grid[row][col] == '0':
        return


    grid[row][col] = '0' # visited node is set to 0 to mark as visited
    dfs(grid, row - 1, col)
    dfs(grid, row + 1, col)
    dfs(grid, row, col - 1)
    dfs(grid, row, col + 1)


# # Solution 3
# ##### DFS with grid modification

# In[ ]:


class Solution:
    
    def numIslands(self, grid):
        
        if not grid:
            return 0
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        island_count = 0
        visited = set()
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1' and (i, j) not in visited:
                    island_count += 1
                    self.dfs(i, j, visited, grid)
                    
                    
        return island_count
    
    def dfs(self, i, j, visited, grid):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == '0' or (i, j) in visited:
            return
        
        
        visited.add((i, j))
            
        self.dfs(i-1, j, visited, grid)
        self.dfs(i+1, j, visited, grid)
        self.dfs(i, j+1, visited, grid)
        self.dfs(i, j-1, visited, grid)


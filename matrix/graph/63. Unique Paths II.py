#!/usr/bin/env python
# coding: utf-8

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:<br>
# 
# Input:<br>
# [<br>
#   [0,0,0],<br>
#   [0,1,0],<br>
#   [0,0,0]<br>
# ]<br>
# Output: 2<br>
# Explanation:<br>
# There is one obstacle in the middle of the 3x3 grid above.<br>
# There are two ways to reach the bottom-right corner:<br>
# 1. Right -> Right -> Down -> Down<br>
# 2. Down -> Down -> Right -> Right

# In[ ]:


def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0

    nrow = len(obstacleGrid)
    ncol = len(obstacleGrid[0])

    aux = [[1 for _ in range(ncol)] for _ in range(nrow)]
    for row in range(1, nrow):
        aux[row][0] = aux[row-1][0] * (1 - obstacleGrid[row][0])

    for col in range(1, ncol):
        aux[0][col] = aux[0][col-1] * (1 - obstacleGrid[0][col])

    for row in range(1, nrow):
        for col in range(1, ncol):
            if obstacleGrid[row][col] == 1:
                aux[row][col] = 0
            else:
                aux[row][col] = aux[row - 1][col] + aux[row][col - 1]

    return aux[-1][-1]


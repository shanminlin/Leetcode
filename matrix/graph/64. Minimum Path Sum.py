#!/usr/bin/env python
# coding: utf-8

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.
# 
# Example:<br>
# 
# Input:<br>
# [<br>
#   [1,3,1],<br>
#   [1,5,1],<br>
#   [4,2,1]<br>
# ]<br>
# Output: 7<br>
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# In[ ]:


def minPathSum(self, grid: List[List[int]]) -> int:
    if not grid:
        return 0

    nrow = len(grid)
    ncol = len(grid[0])

    aux = [[0 for _ in range(ncol)] for _ in range(nrow)]
    aux[0][0] = grid[0][0]

    # first column
    for row in range(1, nrow):
        aux[row][0] = grid[row][0] + aux[row-1][0]

    # first row
    for col in range(1, ncol):
        aux[0][col] = grid[0][col] + aux[0][col-1]

    for row in range(1, nrow):
        for col in range(1, ncol):
            aux[row][col] = grid[row][col] + min(aux[row-1][col], aux[row][col-1])

    return aux[-1][-1]


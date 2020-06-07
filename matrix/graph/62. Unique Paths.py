#!/usr/bin/env python
# coding: utf-8

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?
# Example 1:<br>
# 
# Input: m = 3, n = 2<br>
# Output: 3<br>
# Explanation:<br>
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:<br>
# 1. Right -> Right -> Down<br>
# 2. Right -> Down -> Right<br>
# 3. Down -> Right -> Right<br>
# 
# Example 2:<br>
# Input: m = 7, n = 3<br>
# Output: 28<br>
# 
# Constraints:
# - 1 <= m, n <= 100
# - It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

# In[ ]:


def unique_paths(m, n):
    aux = [[1 for _ in range(n)] for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            aux[i][j] = aux[i][j-1] + aux[i-1][j]
    return aux[-1][-1]


# The above solution runs in O(m * n) time and costs O(m * n) space. However, you may have noticed that each time when we update dp[i][j], we only need dp[i - 1][j] (at the previous row) and dp[i][j - 1] (at the current row). So we can reduce the memory usage to just two rows (O(n)).

# In[ ]:





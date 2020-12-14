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

# Solution 1: recursion, global variable
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.result = 0
        i = j = 0
        target_i = m - 1
        target_j = n - 1
        self.helper(i, j, target_i, target_j)
        return self.result
    
    def helper(self, i, j, target_i, target_j):
        if i == target_i and j == target_j:
            self.result += 1
            return
        if i > target_i or j > target_j:
            return
            
        self.helper(i+1, j, target_i, target_j)
        self.helper(i, j+1, target_i, target_j)

# Solution 2: recursion
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i = j = 0
        target_i = m - 1
        target_j = n - 1
        return self.helper(i, j, target_i, target_j)

    
    def helper(self, i, j, target_i, target_j):
        if i == target_i and j == target_j:
            return 1
        if i > target_i or j > target_j:
            return 0
            
        return self.helper(i+1, j, target_i, target_j) + self.helper(i, j+1, target_i, target_j)


# Solution 3: dynamic programming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n] * m
        for i in range(m):
            dp[i][0] = 1
            
        for j in range(n):
            dp[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]

# The above solution runs in O(m * n) time and costs O(m * n) space. However, you may have noticed that each time when we update dp[i][j], we only need dp[i - 1][j] (at the previous row) and dp[i][j - 1] (at the current row). So we can reduce the memory usage to just two rows (O(n)).





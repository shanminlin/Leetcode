#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Note:
# 
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# # Solution
# - time O(N^2)
# - space O(1)

# In[ ]:


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        # Transpose
        for nrow in range(len(matrix)):
            # Column starts from nrow, if not, change in previous row is reverted
            for ncol in range(nrow, len(matrix)): 
                matrix[nrow][ncol], matrix[ncol][nrow] = matrix[ncol][nrow], matrix[nrow][ncol]
        
        # Reverse each row
        for row in matrix:
            row.reverse()
                


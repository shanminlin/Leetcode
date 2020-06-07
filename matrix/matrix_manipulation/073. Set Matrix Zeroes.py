#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
# 
# Example 1:<br>
# 
# Input: <br>
# [<br>
#   [1,1,1],<br>
#   [1,0,1],<br>
#   [1,1,1]<br>
# ]<br>
# Output: <br>
# [<br>
#   [1,0,1],<br>
#   [0,0,0],<br>
#   [1,0,1]<br>
# ]<br>
# 
# Example 2:
# 
# Input: <br>
# [<br>
#   [0,1,2,0],<br>
#   [3,4,5,2],<br>
#   [1,3,1,5]<br>
# ]<br>
# Output: <br>
# [<br>
#   [0,0,0,0],<br>
#   [0,4,5,0],<br>
#   [0,3,1,0]<br>
# ]<br>
# 
# Follow up:
# A straight forward solution using O(mn) space is probably a bad idea.<br>
# A simple improvement uses O(m + n) space, but still not the best solution.<br>
# Could you devise a constant space solution?<br>

# # Solution
# - time O(N)
# - space O(1)

# In[ ]:


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        first_row_zero = False
        first_col_zero = False
        # Check whether first row and first column contain zero
        for element in matrix[0]:
            if element == 0:
                first_row_zero = True
                break
        
        for element in matrix:
            if element[0] == 0:
                first_col_zero = True
                break
        
        # Modify first row and first column to store zero row and col index
        for nrow in range(1, len(matrix)):
            for ncol in range(1, len(matrix[0])):
                if matrix[nrow][ncol] == 0:
                    matrix[nrow][0] = 0
                    matrix[0][ncol] = 0
                    
        # Modify entire matrix according to first row and column
        for nrow in range(1, len(matrix)):
            for ncol in range(1, len(matrix[0])):
                if matrix[0][ncol] == 0:
                    matrix[nrow][ncol] = 0
                if matrix[nrow][0] == 0:
                    matrix[nrow][ncol] = 0
        
        if first_row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        return matrix


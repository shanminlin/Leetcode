#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# 
# Example 1:<br>
# Input:<br>
# [<br>
#  [ 1, 2, 3 ],<br>
#  [ 4, 5, 6 ],<br>
#  [ 7, 8, 9 ]<br>
# ]<br>
# Output: [1,2,3,6,9,8,7,4,5]<br>
# 
# Example 2:<br>
# Input:<br>
# [<br>
#   [1, 2, 3, 4],<br>
#   [5, 6, 7, 8],<br>
#   [9,10,11,12]<br>
# ]<br>
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# # Solution

# In[10]:


class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        seen = []

        start_row = 0
        end_row = nrow - 1
        start_col = 0
        end_col = ncol - 1
        direction = 0
        while start_row <= end_row and start_col <= end_col:
            # go from left to right
            if direction == 0: 
                for col in range(start_col, end_col + 1):
                    element = matrix[start_row][col]
                    seen.append(element)
                start_row += 1
                direction = 1

            # go from top to bottom
            elif direction == 1:
                for row in range(start_row, end_row + 1):
                    element = matrix[row][end_col]
                    seen.append(element)
                end_col -= 1
                direction = 2

            # go from left to right
            elif direction == 2:
                for col in range(end_col, start_col - 1, -1):
                    element = matrix[end_row][col]
                    seen.append(element)
                end_row -= 1
                direction = 3

            # go from bottom to top
            else:
                for row in range(end_row, start_row - 1, -1):
                    element = matrix[row][start_col]
                    seen.append(element)
                start_col += 1
                direction = 0
        return seen


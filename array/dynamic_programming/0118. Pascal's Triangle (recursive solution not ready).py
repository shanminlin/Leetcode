#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# 
# <img src='./images/triangle.gif'>
# 
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# 
# Example:
# 
# Input: 5<br>
# Output:<br>
# [<br>
#      [1],<br>
#     [1,1],<br>
#    [1,2,1],<br>
#   [1,3,3,1],<br>
#  [1,4,6,4,1]<br>
# ]

# # Brainstorm
# 
# We create the matrix, then fill.
# How to create the matrix?
# - [1] * 2 will be [1, 1]. So use [1] * level to create the list with desired size.
# - For the inside of the list, replace the value of two values from previous level.
# - Time O(N^2), space O(N^2)
# 
# How about a recursive solution?
# - Not so straightforward.
# 

# # Solution 1
# ##### Tabulation

# In[11]:


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        matrix = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, len(matrix[i]) - 1):
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
        
        return matrix


# In[ ]:


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        
        
        triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            level = [1] * (i + 1)
            triangle.append(level)
            for j in range(1, len(level) - 1):
                triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
                
        return triangle


# # Solution 2
# ##### Recursion

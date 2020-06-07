#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two sparse matrices A and B, return the result of AB.
# 
# You may assume that A's column number is equal to B's row number.

# # Brainstorm
# 
# How would we multiply two dense matrices A and B?
# - Take the first row in A and first column in B. Now we have two vectors a and b with the same length.
# - Take first element in a and first element in b, multiple. Do so for all elements in a and b and sum the result. This sum will be the first element in our answer matrix.
# - Repeat for all other rows in A and all other columns in B
# 
# Translate this to code is not so straightforward. The iterators for matrix A and B and the resulting matrix have different lengths. 

# # Solution

# In[12]:


class Solution:
    def multiply(self, A, B):
        
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
                                    
        for rowA in range(len(A)):
            for colA in range(len(A[0])):
                for colB in range(len(B[0])):
                    if A[rowA][colA] != 0 and B[colA][colB] != 0:
                        result[rowA][colB] += A[rowA][colA] * B[colA][colB]
        
        return result


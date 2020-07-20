#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
# 
# Example 1:<br>
# 
# Input:<br>
# A: [1,2,3,2,1]<br>
# B: [3,2,1,4,7]<br>
# Output: 3<br>
# Explanation: <br>
# The repeated subarray with maximum length is [3, 2, 1].
#  
# 
# Note:
# 
# 1 <= len(A), len(B) <= 1000<br>
# 0 <= A[i], B[i] < 100
#  

# # Brainstorm
# 
# 

# In[1]:


memo = [[0, 1, 1], [2, 3, 4]]


# In[5]:


max(max(row) for row in memo)


# In[ ]:


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        
        if not A or not B:
            return 0
        
        memo = [[0] * (len(B) + 1 ) for row in range (len(A) + 1)]
        
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1] + 1
                    
        # max number in the matrix
        max_length = 0
        for row_num in range(len(memo)):
            for col_num in range(len(memo[0])):
                max_length = max(memo[row_num][col_num], max_length)
                
        return max_length


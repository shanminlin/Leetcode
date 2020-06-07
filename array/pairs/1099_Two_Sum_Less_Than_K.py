#!/usr/bin/env python
# coding: utf-8

# # Problem
# Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.
# 
# Example 1:<br>
# Input: A = [34,23,1,24,75,33,54,8], K = 60<br>
# Output: 58<br>
# Explanation:<br>
# We can use 34 and 24 to sum 58 which is less than 60.<br>
# 
# Example 2:<br>
# Input: A = [10,20,30], K = 15<br>
# Output: -1<br>
# Explanation: <br>
# In this case it's not possible to get a pair sum less that 15.
# 
# Note:
# - 1 <= A.length <= 100
# - 1 <= A[i] <= 1000
# - 1 <= K <= 2000

# # Brainstorm
# Start with brute force solution
# - Calculate all sums.
# - Sort all sums.
# - Iterate the sums and stop when the sum exceeds K.
# - Return the previous sum.
# - Time O(N^2), space O(N)
# 
# To reduce time, think of sorting
# - Sort the elements first.
# - Use two pointers. From the two ends of the array

# In[1]:


def twoSumLessThanK(A, K):
    
    A.sort()
    
    low = 0
    high = len(A) - 1
    
    answer = -1
    while low < high:
        curr_sum = A[low] + A[high]
        
        if curr_sum < K:
            answer = max(answer, curr_sum)
            low += 1
        
        else:
            high -= 1
            
    return answer       


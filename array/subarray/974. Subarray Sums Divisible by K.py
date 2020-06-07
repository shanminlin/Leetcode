#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
# 
# 
# Example 1:<br>
# 
# Input: A = [4,5,0,-2,-3,1], K = 5<br>
# Output: 7<br>
# Explanation: There are 7 subarrays with a sum divisible by K = 5:<br>
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]<br>
#  
# 
# Note:
# 
# 1 <= A.length <= 30000<br>
# -10000 <= A[i] <= 10000<br>
# 2 <= K <= 10000

# In[ ]:


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        subarray_sum = {0: 1}
        count = 0
        curr_sum = 0
        for num in A:
            curr_sum += num
            if curr_sum % K in subarray_sum:
                count += subarray_sum[curr_sum % K]
            subarray_sum[curr_sum % K] = subarray_sum.get(curr_sum % K, 0) + 1
        return count


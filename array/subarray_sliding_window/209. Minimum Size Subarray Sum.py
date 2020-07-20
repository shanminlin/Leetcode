#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
# 
# Example:<br>
# 
# Input: s = 7, nums = [2,3,1,2,4,3]<br>
# Output: 2<br>
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.<br>
# 
# Follow up:<br>
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

# # Brainstorm
# 
# Why given positive integers? compare with test cases when there are negative numbers and zeroes.
# 
# 

# In[ ]:


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or not s:
            return 0
        
        min_length = float('inf')
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum >= s:
                    length = j - i + 1
                    min_length = min(min_length, length)
                    break
        
        if min_length == float('inf'):
            return 0
        else:
            return min_length


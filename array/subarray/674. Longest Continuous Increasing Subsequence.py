#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
# 
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
# Note: Length of the array will not exceed 10,000.

# In[6]:


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_count = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1
            
            max_count = max(max_count, count)       
        return max_count


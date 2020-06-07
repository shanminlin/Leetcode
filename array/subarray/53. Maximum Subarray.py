#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# 
# Example:<br>
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],<br>
# Output: 6<br>
# Explanation: [4,-1,2,1] has the largest sum = 6.<br>
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# # Brainstorm
# 
# How to handle negative numbers?
# - If it is at the start or the end of the array, ignore. It will not be in the maximum subarray.
# - If it is in between, store the previous positive number, keep computing the sum, if the sum is positive, include the previous subarray, if not, restart the subarray

# In[ ]:


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # If all numbers are negative:
        count_negative = 0
        for num in nums:
            if num < 0:
                count_negative += 1
        if count_negative == len(nums):
            return max(nums)
        
        max_sum = 0
        curr_sum = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                curr_sum += nums[i]
                max_sum = max(max_sum, curr_sum)
            else:
                if curr_sum + nums[i] < 0:
                    curr_sum = 0
                else:
                    curr_sum += nums[i]
                    
        return max_sum


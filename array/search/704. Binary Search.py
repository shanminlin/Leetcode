#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.<br>
# 
# 
# Example 1:<br>
# 
# Input: nums = [-1,0,3,5,9,12], target = 9<br>
# Output: 4<br>
# Explanation: 9 exists in nums and its index is 4<br>
# 
# Example 2:<br>
# 
# Input: nums = [-1,0,3,5,9,12], target = 2<br>
# Output: -1<br>
# Explanation: 2 does no<br>t exist in nums so return -1
#  
# 
# Note:
# 
# You may assume that all elements in nums are unique.<br>
# n will be in the range [1, 10000].<br>
# The value of each element in nums will be in the range [-9999, 9999].

# # Brainstorm
# 
# Time O(logN), space O(1)

# In[ ]:


class Solution:
    def search(self, nums, target):
        # Edge case: nums is None or empty
        if not nums:
            return -1
        # Edge case: target exceeds range
        if target > nums[-1] or target < nums[0]:
            return -1
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            # If odd length, mid position is the middle
            # If even, mid poistion is the first one between the middle two
            mid = (low + high) // 2
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif mid_num < target:
                low = mid + 1
            else:
                high = mid - 1
                
        # If target not found
        return -1
            


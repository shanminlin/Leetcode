#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.<br>
# 
# Your algorithm's runtime complexity must be in the order of O(log n).<br>
# 
# If the target is not found in the array, return [-1, -1].<br>
# 
# Example 1:<br>
# 
# Input: nums = [5,7,7,8,8,10], target = 8<br>
# Output: [3,4]<br>
# 
# Example 2:<br>
# 
# Input: nums = [5,7,7,8,8,10], target = 6<br>
# Output: [-1,-1]

# # Brainstorm
# 
# Binary search until target found, then continues to walk to left and right to find all targets
# - Time O(N), space O(1)
# 
# To reduce time, we can do binary search after we have found one target.
# - 

# # Solution 1
# ##### Binary search + linear search 

# In[ ]:


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        # binary search
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2 
            mid_num = nums[mid]
            
            if mid_num < target:
                low = mid + 1
            elif mid_num > target:
                high = mid - 1
            else:
                i = j = mid
                # Found target, continue to walk to right
                while i < len(nums) and nums[i] == target:
                    i += 1
                # Found target, continue to walk to left
                while j >= 0 and nums[j] == target:
                    j -= 1
                return [j + 1, i - 1]
        
        return [-1, -1]


# # Solution 2
# ##### 2 binary search

# In[ ]:


class Solution:
    def searchRange(self, nums, target):
        if nums == []:
            return [-1, -1]
        
        target_range = [-1, -1]
        
        # Binary search to find the leftmost index of target
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2 # mid towards low
            mid_num = nums[mid]
            
            if target == mid_num:
                high = mid
            elif target < mid_num:
                high = mid - 1
            else:
                low = mid + 1
        
        # If target found, low == high; if target not found, high == -1
        # so usng both low or high is ok; high will not be out of list range
        if nums[low] == target: 
            target_range[0] = low
        
        # Binary search to find the rightmost index of target
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2 + 1 # mid towards high
            mid_num = nums[mid]
            
            if target == mid_num:
                low = mid
            elif target < mid_num:
                high = mid - 1
            else:
                low = mid + 1
        
        # If target not found, low == len(nums), out of range
        # So we can only use high pointer
        if nums[high] == target: 
            target_range[1] = high
            
        return target_range


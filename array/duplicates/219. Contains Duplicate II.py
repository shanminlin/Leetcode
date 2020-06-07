#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
# 
# Example 1:<br>
# 
# Input: nums = [1,2,3,1], k = 3<br>
# Output: true<br>
# 
# Example 2:<br>
# 
# Input: nums = [1,0,1,1], k = 1<br>
# Output: true<br>
# 
# Example 3:
# 
# Input: nums = [1,2,3,1,2,3], k = 2<br>
# Output: false

# # Brainstorm
# 
# In addition to find the duplicates, we need to keep track of the index of the each element so that we can know the distance between current and previousely seen elements.

# # Solution

# In[ ]:


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if not nums or k == 0:
            return False
        
        seen = {}
        min_distance = float('inf')
        for i, num in enumerate(nums):
            if num in seen:
                distance = i - seen[num]
                min_distance = min(min_distance, distance)
                seen[num] = i
            else:
                seen[num] = i
                
        return min_distance <= k


# Simplify code, no need to keep a min_distance variable:

# In[ ]:


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if not nums or k == 0:
            return False
        
        # Use a dictionary to keep track
        # seen elements and their indices
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                distance = i - seen[num]
                if distance <= k:
                    return True
            seen[num] = i
                
        return False
                


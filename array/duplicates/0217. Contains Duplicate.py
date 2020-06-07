#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of integers, find if the array contains any duplicates.
# 
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
# 
# Example 1:<br>
# Input: [1,2,3,1]<br>
# Output: true<br>
# 
# Example 2:<br>
# Input: [1,2,3,4]<br>
# Output: false<br>
# 
# Example 3:<br>
# Input: [1,1,1,3,3,4,3,2,4,2]<br>
# Output: true<br>

# # Brainstorm
# Start with brute force
# - for each element, compare with every other element in the rest of the array
# - Time O(N^2), space O(1)
# 
# Hash table
# - Time O(N), space O(N)
# 
# Sort (check whether we can modify the original array)
# - Iterate time O(N), sorting O(NlogN) so overall time is dominated by sorting O(NlogN); space O(1)

# # Solution 1
# ##### Brute force

# In[2]:


class Solution:
    def containsDuplicate(self, nums):
        
        if not nums:
            return False
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# # Solution 2
# ##### Hash table

# In[ ]:


class Solution:
    def containsDuplicate(self, nums):
        # Special cases
        if not nums:
            return False
        
        if len(nums) == 1:
            return False
        
        # Compare elements with previously
        # seen elements
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# # Solution 3
# ##### Sort

# In[ ]:


class Solution:
    def containsDuplicate(self, nums):
        # Special cases
        if not nums:
            return False
        
        if len(nums) == 1:
            return False
        
        nums.sort()
        
        # Compare adjacent elements
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


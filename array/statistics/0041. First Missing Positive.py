#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an unsorted integer array, find the smallest missing positive integer.<br>
# 
# Example 1:<br>
# 
# Input: [1,2,0]<br>
# Output: 3<br>
# 
# Example 2:<br>
# 
# Input: [3,4,-1,1]<br>
# Output: 2<br>
# 
# Example 3:<br>
# 
# Input: [7,8,9,11,12]<br>
# Output: 1<br>
# 
# Note:<br>
# Your algorithm should run in O(n) time and uses constant extra space.

# # Brainstorm
# 
# Start with a brute force
# - Sort the array.
# - For the positive part of the array, compare it with a set containing 1 to max of the positive array.
# - Remove numbers from the array that are also present in the set
# - The smallest number in the set is now what we want.
# 
# First, can we reduce the search space?
# - If the array is all positive from 1 to length - 1, the smallest missing positive is between 1 and n + 1.
# 
# Can we eliminate the set?
# - if the array is [5, 2, 4], the set will be just {1, 2, 3, 4}
# - It seems that the set is like the index of an array.
# 

# In[1]:


nums = [1, 2]
nums.insert(0, 0)


# In[2]:


nums


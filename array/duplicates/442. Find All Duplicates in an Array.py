#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# 
# Find all the elements that appear twice in this array.
# 
# Could you do it without extra space and in O(n) runtime?
# 
# Example:<br>
# Input:<br>
# [4,3,2,7,8,2,3,1]<br>
# 
# Output:<br>
# [2,3]<br>

# # Brainstorm
# 
# How can we make use use of the two pieces of information?
# - duplicates occur twice
# - the elements in the array are from 1 to n
# - Can we modify the given array?

# # Solution

# In[ ]:


class Solution:
    def findDuplicates(self, nums):
        if not nums:
            return []
        
        duplicates = []
        for num in nums:
            num = abs(num)
            
            # Use index to represent the number,
            # the sign of the value is whether we 
            # have seen the number before
            # num-1 because index starts from zero, number starts from 1
            if nums[num-1] < 0: 
                duplicates.append(num)
            else:
                nums[num-1] *= -1
        
        return duplicates
        


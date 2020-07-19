#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.<br>
# 
# Example:<br>
# 
# Input: [0,1,0,3,12]<br>
# Output: [1,3,12,0,0]<br>
# 
# Note:
# 
# You must do this in-place without making a copy of the array.<br>
# Minimize the total number of operations.<br>

# # Brainstorm
# 
# In-place sorting algorithms are bubble sort, selection sort, insertion sort, quick sort.
# 
# Selection sort is not suitable as it will change the position of non-zero elements.
# 
# Bubble sort is ok but too many swaps and iterations.
# 
# Insertion sort is good as not too many iterations compared to bubble sort.
# - but too many cases to skip the swaps.
# 
# In place quick sort change the order?

# # Solution 1
# ##### Bubble sort

# In[ ]:


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Edge cases
        if not nums or len(nums) == 1:
            return nums
        
        
        finished = False
        while not finished:
            num_of_swaps = 0
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i+1] != 0:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    num_of_swaps += 1
                    
            if num_of_swaps == 0:
                finished = True
                
        return nums


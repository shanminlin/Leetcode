#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# 
# Example:<br>
# 
# Input: nums = [3,5,2,1,6,4]<br>
# Output: One possible answer is [3,5,1,6,2,4]<br>

# # Brainstorm
# 
# List out possible scenaria and swap.

# In[ ]:


class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
    
        """
        if not nums or len(nums) == 1:
            return
        
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
            return

        for i in range(1, len(nums)-1, 2):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
        if nums[-1] < nums[-2] and len(nums) % 2 == 0:
            nums[-1], nums[-2] = nums[-2], nums[-1]


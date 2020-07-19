#!/usr/bin/env python
# coding: utf-8

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

# # Brainstorm
# 

# My wrong solution. It does not handle the case when there are two groups of two_sums. and does not handle duplicate three sums.

# In[ ]:


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        
        three_sum = []    
        for i in range(len(nums) - 3):
            complement = 0 - nums[i]
            two_sum_elements = self.two_sum(nums[i + 1:], complement)
            if two_sum_elements:
                two_sum_elements.append(nums[i])
                three_sum += [two_sum_elements]
                
        return three_sum
    
    def two_sum(self, nums, target):
        nums_set = set()
        for num in nums:
            complement = target - num
            if complement in nums_set:
                return [complement, num]
            nums_set.add(num)


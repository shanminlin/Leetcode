#!/usr/bin/env python
# coding: utf-8

# Problem
# 
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution:
    def permute(self, nums):

        if not nums:
            return []
        
        temp_list = []
        result = []
        self.helper(nums, temp_list, result)
        return result
    
    def helper(self, nums, temp_list, result):
        if len(nums) == 0:
            result.append(temp_list)
            
        for i in range(len(nums)):
            # exclude nums[i] in the recursive function
            self.helper(nums[:i]+nums[i+1:], temp_list+[nums[i]], result)
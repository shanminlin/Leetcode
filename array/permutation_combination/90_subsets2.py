#!/usr/bin/env python
# coding: utf-8

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]

Output: [[2], [1], [1,2,2], [2,2], [1,2], []]
"""
# Solution 1
# keep a slice of nums for each recursive function
class Solution:
    def subsetsWithDup(self, nums):    
        if not nums:
            return []
        
        nums.sort()
        temp_list = []
        result = []
        self.dfs(nums, temp_list, result)
        return result
    
    def dfs(self, nums, temp_list, result):
        result.append(temp_list)
        
        for i in range(len(nums)):
            # skip duplicates
            if i != 0 and nums[i] == nums[i-1]:
                continue
            else:
                self.dfs(nums[i+1:], temp_list+[nums[i]], result)

# Solution 2:
# use indices instead of slicing a list
class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        
        nums.sort()
        temp_list = []
        result = []
        start = 0
        self.dfs(nums, start, temp_list, result)
        return result
    
    def dfs(self, nums, start, temp_list, result):
        result.append(temp_list)
        
        for i in range(start, len(nums)):
            # skip duplicates
            if i != start and nums[i] == nums[i-1]:
                continue
            else:
                self.dfs(nums, i+1, temp_list+[nums[i]], result)



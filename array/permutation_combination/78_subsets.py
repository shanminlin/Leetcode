#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a set of distinct integers, nums, return all possible subsets (the power set).<br>
# 
# Note: The solution set must not contain duplicate subsets.<br>
# 
# Example:<br>
# Input: nums = [1,2,3]<br>
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution:
    def subsets(self, nums):
        temp_list = []
        result = []
        self.dfs(nums, temp_list, result)
        return result
    
    def dfs(self, nums, temp_list, result):
        result.append(temp_list)
        
        if len(nums) == 0:
            return
        
        for i in range(len(nums)):
            self.dfs(nums[i+1:], temp_list+[nums[i]], result)

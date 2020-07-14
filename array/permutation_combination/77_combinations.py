#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.<br>
# 
# Example:<br>
# Input: n = 4, k = 2<br>
# Output:<br>
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    def combine(self, n, k):
        if n == 0:
            return []
        
        nums = [i for i in range(1, n+1)]
        result = []
        temp_list = []
        self.helper(nums, k, temp_list, result)
        return result
    
    def helper(self, nums, k, temp_list, result):
        if len(temp_list) == k:
            result.append(temp_list)
            
        for i in range(len(nums)):
            self.helper(nums[i+1:], k, temp_list+[nums[i]], result)


# faster solution:
# make use of the fact that the numbers are 1 to n
class Solution:
    def combine(self, n, k):
        if n == 0:
            return []
        
        start = 1
        result = []
        temp_list = []
        self.helper(n, k, start, temp_list, result)
        return result
    
    def helper(self, n, k, start, temp_list, result):
        if len(temp_list) == k:
            result.append(temp_list)
            
        for i in range(start, n+1):
            self.helper(n, k, i+1, temp_list+[i], result)
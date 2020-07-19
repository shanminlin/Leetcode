#!/usr/bin/env python
# coding: utf-8

"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
# Solution 1
# dfs using list slicing

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        temp_list = []
        nums = [i for i in range(1, 10)]
        self.helper(k, n, result, temp_list, nums)
        return result
    
    def helper(self, k, n, result, temp_list, nums):
        if sum(temp_list) == n and len(temp_list) == k:
            result.append(temp_list)
            return
            
        elif sum(temp_list) > n or len(temp_list) > k:
            return
        
        else:
            for i, num in enumerate(nums):
                self.helper(k, n, result, temp_list+[num], nums[i+1:])

# Solution 2
# dfs using indices
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        temp_list = []
        nums = [i for i in range(1, 10)]
        start_index = 0
        self.helper(k, n, result, temp_list, nums, start_index)
        return result
    
    def helper(self, k, n, result, temp_list, nums, start_index):
        if sum(temp_list) == n and len(temp_list) == k:
            result.append(temp_list)
            return
            
        elif sum(temp_list) > n or len(temp_list) > k:
            return
        
        else:
            for i in range(start_index, len(nums)):
                self.helper(k, n, result, temp_list+[nums[i]], nums, i+1)

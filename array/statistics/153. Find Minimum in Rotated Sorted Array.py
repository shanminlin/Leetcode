#!/usr/bin/env python
# coding: utf-8

# # Problem 
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.<br>
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).<br>
# 
# Find the minimum element.<br>
# 
# You may assume no duplicate exists in the array.<br>
# 
# Example 1:<br>
# 
# Input: [3,4,5,1,2] <br>
# Output: 1<br>
# 
# Example 2:<br>
# 
# Input: [4,5,6,7,0,1,2]<br>
# Output: 0

# Solution 1
# O(N) time

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_value = nums[0]
        max_value = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min_value:
                min_value = nums[i]
                return min_value

        return min_value

# Solution 2
# O(logN)binary search


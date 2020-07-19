#!/usr/bin/env python
# coding: utf-8

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

# # Brainstorm
# 
# Vanila binary search until low reaches high. 
# - If the value and the target are equal, return index
# - If the value < target, insert at index + 1
# - if the value > target, insert at index
# 
# Time O(logN), space O(1)

# # Solution



class Solution:
    def searchInsert(self, nums, target):
        if nums == []:
            return 0
        
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            mid_num = nums[mid]
            
            if mid_num == target:
                return mid
            elif mid_num < target:
                low = mid + 1
            else:
                high = mid - 1
         
        
        # We have reach low == high
        # and that element has not been checked
        if nums[low] == target:
            return low
        elif nums[low] < target:
            return low + 1 # insert at one position higher 
        else:
            # if target is smaller than the final value, 
            # insert at the final value's position
            return low 
            


# Simplify code:
class Solution:
    def searchInsert(self, nums, target):
        if nums == []:
            return 0
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_num = nums[mid]
            
            if mid_num == target:
                return mid
            elif mid_num < target:
                low = mid + 1
            else:
                high = mid - 1
         
        # Now target is not found, we need to decide where to insert
        # At the final step of the above iteration,
        # if the last searched element < target, 
        # we should insert at the position of last searched element + 1, while is the current low
        # If the last searched element > target,
        # we should insert at the position of last searched element, which is also the current low
        return low


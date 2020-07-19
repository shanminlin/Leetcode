#!/usr/bin/env python
# coding: utf-8

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

# # Brainstorm
# 
# What are the possible scenratios? It might be a little messy to find the patten directly. To simplify, we can first find the pivot, which is the smallest element in the array. Then compare the last element with the pivot to decide on which side to do normal binary search.<br>
# To find the pivot (minimum) is O(N). To reduce to O(logN), use a binary search approach.
# - Overall time is O(logN), space is O(1).

# In[ ]:


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Edge case
        if not nums:
            return -1
        
        
        # Find the pivot
        low = 0
        high = len(nums) - 1
        pivot = high
        
        while low <= high:
            mid = (low + high) // 2
            mid_num = nums[mid]
            pivot_num = nums[pivot]
            
            if pivot_num < mid_num:
                # pivot on the right of mid, not including mid
                low = mid + 1
            elif pivot_num > mid_num:
                # pivot_num >= mid_num
                # pivot on the left of mid, including mid
                high = mid
                pivot = high
            else:
                break

                
        # loop ends when pivot found
        # now pivot = mid = low = high
        if target == nums[pivot]:
            return pivot
        elif target < nums[pivot]:
            return -1
        else:
            right_search = self.binary_search(nums, pivot+1, len(nums)-1, target)
            if right_search != -1:
                return right_search
            else:
                return self.binary_search(nums, 0, pivot-1, target)
            
    def binary_search(self, nums, low, high, target):
        
        while low <= high:
            mid = (low + high) // 2
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif target > mid_num:
                low = mid + 1
            else:
                high = mid - 1
        return -1
            


# Small optimization: 
# - after pivot found, compare nums[-1] with pivot to decide which side of pivot to perform binary search.

# In[ ]:


class Solution:
    def search(self, nums, target):
        # Edge case
        if not nums:
            return -1
        
        # Find the pivot
        low = 0
        high = len(nums) - 1
        pivot = high
        
        while low <= high:
            mid = (low + high) // 2
            mid_num = nums[mid]
            pivot_num = nums[pivot]
            
            if pivot_num < mid_num:
                # pivot on the right of mid, not including mid
                low = mid + 1
            elif pivot_num > mid_num:
                # pivot_num >= mid_num
                # pivot on the left of mid, including mid
                high = mid
                pivot = high
            else:
                break

                
        # loop ends when pivot found
        # now pivot = mid = low = high
        if target == nums[pivot]:
            return pivot
        elif target < nums[pivot]:
            return -1
        else:
            if target > nums[-1]:
                return self.binary_search(nums, 0, pivot-1, target)
            else:
                return self.binary_search(nums, pivot+1, len(nums)-1, target)
            
    def binary_search(self, nums, low, high, target):
        
        while low <= high:
            mid = (low + high) // 2
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif target > mid_num:
                low = mid + 1
            else:
                high = mid - 1
        return -1


# In[ ]:





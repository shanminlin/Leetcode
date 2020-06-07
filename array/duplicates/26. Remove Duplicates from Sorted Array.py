#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# 
# Example 1:<br>
# 
# Given nums = [1,1,2],<br>
# 
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.<br>
# 
# It doesn't matter what you leave beyond the returned length.<br>
# 
# Example 2:
# 
# Given nums = [0,0,1,1,1,2,2,3,3,4],<br>
# 
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.<br>
# 
# It doesn't matter what values are set beyond the returned length.

# # Brainstorm
# 
# The above example tells us that the goal of the problem is to keep unique values in the first length of n, not delete the duplicate elements. The delete operation costs time.
# - Time O(N), space O(1).

# # Solution

# In[ ]:


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        # i and j are initially adjacent
        # If the numbers at i and j are different, 
        # increment both i and j to compare the next adjacent pair
        # If they are the same, increment j to find the nearest nonduplicate
        # fill i+1 (original same as i) with j
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                # Increment j to find next nonduplicate
                continue
            else:
                # Found nonduplicate, modify i+1 value to be j
                # We have to keep copying all values after j to i+1
                # This also holds when i and j are adjacent and distinct,
                # in this case, i+1 is just j
                i += 1
                nums[i] = nums[j]
        
        # i is index, we want to return length
        # so i + 1 to get the length
        return i + 1


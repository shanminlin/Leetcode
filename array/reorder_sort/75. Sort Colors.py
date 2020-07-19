#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.<br>
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.<br>
# 
# Note: You are not suppose to use the library's sort function for this problem.<br>
# 
# Example:<br>
# 
# Input: [2,0,2,1,1,0]<br>
# Output: [0,0,1,1,2,2]<br>
# 
# Follow up:<br>
# 
# A rather straight forward solution is a two-pass algorithm using counting sort.<br>
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.<br>
# Could you come up with a one-pass algorithm using only constant space?<br>

# # Brainstorm
# 
# What are the differences between this problem and normal sorting problems?
# - only 3 types of values: 0, 1, 2
# 
# Note that we want constant space solution, so we probably need to swap elements around.<br>
# 
# With only three values, it is very close to sorted. So think about two or multiple pointers that help iterate and swap.<br>
# 
# This is the Dutch National flag problem. It is hard to come up with the O(N) time and O(1) space solution. <br>

# # Solution

# The following for loop does not work because after swapping current number with high, we have to evaluate current number again. This is different from other conditions when current number is 0 or 1.

# In[ ]:


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        high = len(nums) - 1
        
        for i in range(len(nums)):
            if i > high:
                break
                
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                
            elif nums[i] == 1:
                continue
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
                # How to keep the same i and evaluate again?


# Use a while loop to address that problem.

# In[ ]:


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1
        i = 0
        
        # Loop ends when i crosses high
        # because when i reaches high, value at i not evaluate yet.
        while i <= high:
            
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                i += 1

            elif nums[i] == 1:
                i += 1
            else:
                # Have to check again after swapping
                # so don't increment i
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1


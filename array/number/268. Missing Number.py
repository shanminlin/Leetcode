#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# 
# Example 1:
# 
# Input: [3,0,1]
# Output: 2
# Example 2:
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# In[2]:


# Solution 1
def missingNumber(self, nums):
    if not nums:
        return 0

    max_num = len(nums) + 1

    all_nums = set([n for n in range(max_num + 1)])

    for num in nums:
        all_nums.remove(num)

    return all_nums.pop()


# In[3]:


# Solution 2:
def missingNumber(self, nums):
    if not nums:
        return 0

    max_num = len(nums) + 1

    nums_set = set(nums)

    for num in range(max_num + 1):
        if num not in nums_set:
            return num


# In[4]:


# Solution 3
# a number XOR itself will become 0, any number XOR with 0 will stay unchanged.
def missingNumber(self, nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


#!/usr/bin/env python
# coding: utf-8

# # Problem
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# Example:<br>
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# # Brainstorm
# ##### Start with a brute force solution
# - Compute all possible sums. 
# - This can be done by iterating the array and for each iteration, iterate the rest of the array again. 
# - If the sum is equal to the target, we will return the indices of the elements. 
# - Time O(N^2), space O(1).
# 
# ##### To reduce the time, we think of ways to trade space for time. So we need to store some kinds of values as we iterate.
# - During iteration, at a particular element, compute its complement, and check whether the complement is in the array.
# - For faster check, we store elements in a dictionary.
# - As there may be duplicate elements, we build the dictionary as we iterate and check.
# - This is to check previous elements as we iterate.
# - Time O(N), space O(N).
# 
# ##### To further reduce space, think of pointers
# - Sort the elements in ascending order. As we need to keep the original index, we have to use additional space.
# - Start pointer at the start of the array, end pointer at the end of the array
# - Compute the sum at the two pointers. If the sum is smaller than the target, increment the start pointer to increase sum. If the sum is larger than the target, decrement the end pointer to reduce the sum. If the sum equals the target, return the pointers.
# - When to stop iteration? start pointer equals end pointer.
# - Time O(N), space O(N).

# # Solution 1 
# #####  Brute force

# In[1]:


def two_sum(nums, target):
    # edge cases
    if not nums:
        return []
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# # Solution 2 
# ##### Hash table 

# In[2]:


def two_sum(nums, target):
    # edge cases
    if not nums:
        return []

    nums_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [i, nums_dict[complement]] 
        nums_dict[num] = i


# # Solution 3
# ##### Two pointer

# In[3]:


def two_sum(nums, target):
    # edge cases
    if not nums:
        return []

    nums_sort = [(num, index) for index, num in enumerate(nums)]
    nums_sort.sort()

    low = 0
    high = len(nums) - 1

    while low < high:
        curr_sum = nums_sort[low][0] + nums_sort[high][0]
        if curr_sum < target:
            low += 1
        elif curr_sum > target:
            high -= 1
        else:
            return [nums_sort[low][1], nums_sort[high][1]]


# #### My wrong solution
# It does not pass the test case [3, 3], target = 6. This is because dictionary does not store duplicate keys.

# In[4]:


def two_sum(nums, target):
    # edge cases
    if not nums:
        return []

    nums_dict = {num: index for index, num in enumerate(nums)}

    for i, num in enumerate(nums):
        nums_dict.pop(num)
        complement = target - num
        if complement in nums_dict:
            return [i, nums_dict[complement]] 


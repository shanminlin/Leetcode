#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:<br>
# 
# Input: [1,2,3]<br>
# Output:<br>
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# # Brainstorm 

# In[21]:


def permute(nums):

    current_list = []
    all_lists = []

    return permute_helper(nums, current_list, all_lists)

def permute_helper(nums, current_list, all_lists):
    if nums == []:
        all_lists.append(current_list)

    for i in range(len(nums)):
        permute_helper(nums.remove(nums[i]), current_list+[nums[i]], all_lists) # this removes nums for nodes at the same level

    return all_lists


# remove elements from a collection while iterating it leads to None.

# Solution 1: bfs

# In[1]:


def permute(nums):
    permutations = []
    dfs(nums, [], permutations)
    return permutations

def dfs(nums, templist, permutations):
    if not nums:
        permutations.append(templist)
        #return # backtracking
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], templist+[nums[i]], permutations)


# In[2]:


nums = [1, 2, 3]
permute(nums)


# Solution 2: backtrack

# In[5]:


def permute_backtrack(nums):
    permutations = []
    backtrack(nums, 0, permutations)
    return permutations

def backtrack(nums, start, permutations):
    if start == len(nums):
        permutations.append(nums[:])
        
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        backtrack(nums, start+1, permutations)
        nums[start], nums[i] = nums[i], nums[start]


# In[6]:


nums = [1, 2, 3]
permute_backtrack(nums)


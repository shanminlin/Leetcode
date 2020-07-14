#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a collection of integers that might contain **duplicates**, nums, return all possible subsets (the power set).
# 
# Note: 
# - The solution set must not contain duplicate subsets.
# 
# Example:<br>
# Input: [1,2,2]<br>
# Output:<br>
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# # Brainstorm
# 
# 

# Solution 1: BFS

# In[3]:


def subsets_withdup(nums):
    subsets = []
    nums.sort()
    dfs(nums, 0, [], subsets)
    return subsets
    
def dfs(nums, start, templist, subsets):
    subsets.append(templist)
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:
            continue
        dfs(nums, i+1, templist+[nums[i]], subsets)


# In[4]:


nums = [1, 2, 2]
subsets_withdup(nums)


# Solution 2: backtrack

# In[7]:


def subsets_withdup_backtrack(nums):
    subsets = []
    nums.sort()
    backtrack(nums, 0, [], subsets)
    return subsets

def backtrack(nums, start, templist, subsets):
    subsets.append(templist[:])
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:
            continue
        templist.append(nums[i])
        backtrack(nums, i+1, templist, subsets)
        templist.pop()


# In[8]:


nums = [1, 2, 2]
subsets_withdup_backtrack(nums)


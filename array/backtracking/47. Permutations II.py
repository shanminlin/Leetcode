#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.<br>
# 
# Example:<br>
# Input: [1,1,2]<br>
# Output:<br>
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# # Brainstorm

# Solution 1: BFS

# In[2]:


def permute_unique(nums):
    permutations = []
    visited = [False]*len(nums)
    nums.sort()
    dfs(nums, visited, [], permutations)
    return permutations
    
def dfs(nums, visited, templist, permutations):
    if len(nums) == len(templist):
        permutations.append(templist)
        return 
    for i in range(len(nums)):
        if not visited[i]: 
            if i > 0 and not visited[i-1] and nums[i] == nums[i-1]:  # here should pay attention
                continue
            visited[i] = True
            dfs(nums, visited, templist+[nums[i]], permutations)
            visited[i] = False


# In[3]:


nums = [1, 1, 2]
permute_unique(nums)


# Solution 2: backtrack

# In[4]:


def permute_unique_backtrack(nums):
    permutations = []
    visited = [False] * len(nums)
    nums.sort()
    backtrack(nums, [], visited, permutations)
    return permutations
    
def backtrack(nums, templist, visited, permutations):
    if len(templist) == len(nums):
        permutations.append(templist[:])
    else:
        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                continue
            visited[i] = True
            templist.append(nums[i])
            backtrack(nums, templist, visited, permutations)
            templist.pop()
            visited[i] = False


# In[5]:


nums = [1, 1, 2]
permute_unique_backtrack(nums)


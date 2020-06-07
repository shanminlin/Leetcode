#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.<br>
# 
# Example:<br>
# Input: n = 4, k = 2<br>
# Output:<br>
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# # Brainstorm
# 
# 

# In[ ]:


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        all_subsets = []
        subset = []
        start_index = 0
        return self.helper(n, k, start_index, subset, all_subsets)
    
    def helper(self, n, k, start_index, subset, all_subsets):
        if len(subset) == k:
            all_subsets.append(subset)
            return
        
        for i in range(start_index, n):
            self.helper(n, k, i+1, subset+[i+1], all_subsets)
        
        return all_subsets


# In[3]:


def combine(n, k):
    combinations = []
    nums = range(1, n+1)
    dfs(nums, k, 0, [], combinations)
    return combinations
    
def dfs(nums, k, start, templist, combinations):
    if k == 0:
        combinations.append(templist)
        return # backtracking 
    for i in range(start, len(nums)):
        dfs(nums, k-1, i+1, templist+[nums[i]], combinations)


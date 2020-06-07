#!/usr/bin/env python
# coding: utf-8

# # Problem
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target. The same repeated number may be chosen from candidates unlimited number of times.
# 
# Note:
# 
# - All numbers (including target) will be positive integers.
# - The solution set must not contain duplicate combinations.
# 
# Example 1:<br>
# Input: candidates = [2,3,6,7], target = 7,<br>
# A solution set is:<br>
# [
#   [7],
#   [2,2,3]
# ]
# 
# Example 2:<br>
# Input: candidates = [2,3,5], target = 8,<br>
# A solution set is:<br>
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

# # Brainstorm
# 
# 
# 
# 

# # Solution 1
# ##### dfs

# In[ ]:


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subset = []
        all_subsets = []
        loop_start = 0
        return self.helper(candidates, target, loop_start, subset, all_subsets)
    
    def helper(self, candidates, target, loop_start, subset, all_subsets):
        
        if sum(subset) > target:
            return
        elif sum(subset) == target:
            all_subsets.append(subset)
            return
            
        for i in range(loop_start, len(candidates)):
            self.helper(candidates, target, i, subset+[candidates[i]], all_subsets)
            
        return all_subsets


# In[4]:


def combination_sum(candidates, target):
    subsets = []
    candidates.sort()
    dfs(candidates, target, 0, [], subsets)
    return subsets
    
def dfs(candidates, target, start, templist, subsets):
    if target < 0:
        return  # backtracking
    if target == 0:
        subsets.append(templist)
        return 
    for i in range(start, len(candidates)):
        dfs(candidates, target-candidates[i], i, templist+[candidates[i]], subsets)


# My wrong solution, which counted duplicate combinations:

# In[ ]:


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subset = []
        all_subsets = []
        return self.helper(candidates, target, subset, all_subsets)
    
    def helper(self, candidates, target, subset, all_subsets):
        
        if sum(subset) > target:
            return
        elif sum(subset) == target:
            all_subsets.append(subset)
            return
            
        for i in range(len(candidates)):
            self.helper(candidates, target, subset+[candidates[i]], all_subsets)
            
        return all_subsets


# # Solution 2: backtracking

# In[9]:


def combination_sum_backtrack(candidates, target):
    subsets = [] 
    candidates.sort(reverse=True)
    backtrack(candidates, target, 0, [], subsets)
    return subsets
    
def backtrack(candidates, target, start, templist, subsets):
    if target == 0:
        subsets.append(templist[:])
    elif target > 0:
        for i in range(start, len(candidates)):
            templist.append(candidates[i])
            backtrack(candidates, target-candidates[i], i, templist, subsets)
            templist.pop()


# In[10]:


candidates = [2, 3, 5]
target = 8
combination_sum_backtrack(candidates, target)


# # Solution 3: bottom up dynamic programming

# In[33]:


def combinationSum(candidates, target):

    if not candidates or not target:
        return []

    aux = [[] for _ in range(target + 1)]
    aux[0].append([]) # this is because [[2] + comb for comb in []] will be []. 

    for val in candidates:
        for i in range(val, 1+target):
            dp[i].extend(comb+[val] for comb in dp[i-val])
    return dp[target]


# In[52]:


a = [[2, 2]]
a.extend([2] + comb for comb in [[]])
print(a)


# In[51]:


[[2] + comb for comb in [[]]]


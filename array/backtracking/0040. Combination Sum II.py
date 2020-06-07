#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target. Each number in candidates may only be used once in the combination.
# 
# Note:
# - All numbers (including target) will be positive integers.
# - The solution set must not contain duplicate combinations.
# 
# Example 1:<br>
# Input: candidates = [10,1,2,7,6,1,5], target = 8,<br>
# A solution set is:<br>
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 
# Example 2:<br>
# Input: candidates = [2,5,2,1,2], target = 5,<br>
# A solution set is:<br>
# [
#   [1,2,2],
#   [5]
# ]

# # Brainstorm
# 
# 

# In[1]:


a = [2, 5, 2, 1, 2]


# In[2]:


all_combinations = []


# In[4]:


for i in range(len(a)):
    combination = []
    for j in range(i+1, len(a)):
        combination.append([a[i], a[j]])
    all_combinations.append(combination)        


# In[5]:


all_combinations


# # Solution 1: top down dynamic programming (dfs)

# In[ ]:


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        all_subsets = []
        subset = []
        start_index = 0
        return self.helper(candidates, target, start_index, subset, all_subsets)
    
    def helper(self, candidates, target, start_index, subset, all_subsets):
        
        if sum(subset) > target:
            return
        elif sum(subset) == target:
            all_subsets.append(subset)
            return
        
        for i in range(start_index, len(candidates)):
            if candidates[i] == candidates[i-1] and i > start_index:
                continue
                
            self.helper(candidates, target, i+1, subset+[candidates[i]], all_subsets)
            
        return all_subsets


# In[1]:


def combination_sum2(candidates, target):
    result = []
    candidates.sort()
    dfs(candidates, target, 0, [], result)
    return result
    
def dfs(candidates, target, start, templist, result):
    if target < 0:
        return  
    if target == 0:
        result.append(templist)
        return  
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i-1]:
            continue
        dfs(candidates, target-candidates[i], i+1, templist+[candidates[i]], result)


# Solution 2: Backtracking

# In[5]:


def combination_sum2_backtrack(candidates, target):
    subsets = []
    candidates.sort(reverse=True)
    backtrack(candidates, target, 0, [], subsets)
    return subsets

def backtrack(candidates, target, start, templist, subsets):
    if target == 0:
        subsets.append(templist[:])
        
    elif target > 0:
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            templist.append(candidates[i])
            backtrack(candidates, target-candidates[i], i+1, templist, subsets)
            templist.pop()   


# # Solution 3: bottom up dynamic programming

# In[ ]:


def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    aux = [set() for i in range(target + 1)]
    aux[0].add(())
    for candidate in candidates:
        for subtarget in range(target, candidate - 1, -1):
            for prev in aux[subtarget - candidate]:
                aux[subtarget].add(prev + (candidate,))
    return list(aux[-1])


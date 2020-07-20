#!/usr/bin/env python
# coding: utf-8

"""
Problem
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target. The same repeated number may be chosen from candidates unlimited number of times.

Note:
- All numbers (including target) will be positive integers.
- The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
[7],
[2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
[2,2,2,2],
[2,3,3],
[3,5]
]
"""

# # Solution 1
# dfs using list slicing
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates:
            return []
        
        result = []
        temp_list = []
        self.helper(candidates, temp_list, result, target)
        return result
    
    def helper(self, candidates, temp_list, result, target):
        
        if sum(temp_list) == target:
            result.append(temp_list)
            return
            
        elif sum(temp_list) < target:
            for i, candidate in enumerate(candidates):
                self.helper(candidates[i:], temp_list+[candidate], result, target)
        
        else:
            return


# Solution 2:
# dfs using indices

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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




# My wrong solution, which counted duplicate combinations:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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


# # Solution 3: backtracking
def combination_sum_backtrack(candidates, target):
    subsets = [] 
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




# # Solution 4: bottom up dynamic programming
def combinationSum(candidates, target):

    if not candidates or not target:
        return []

    dp = [[] for _ in range(target + 1)]
    dp[0].append([]) # this is because [[2] + comb for comb in []] will be []. 

    for val in candidates:
        for i in range(val, 1+target):
            dp[i].extend(comb+[val] for comb in dp[i-val])
    return dp[target]
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


# Solution 1
# dfs using list slicing
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()
        
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
                if candidates[i] == candidates[i-1] and i != 0:
                    continue
                else:
                    self.helper(candidates[i+1:], temp_list+[candidate], result, target)
        
        else:
            return
        
        
# Solution 2
# dfs using indices
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


# Solution 3: Backtracking

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


# # Solution 4: bottom up dynamic programming

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    aux = [set() for i in range(target + 1)]
    aux[0].add(())
    for candidate in candidates:
        for subtarget in range(target, candidate - 1, -1):
            for prev in aux[subtarget - candidate]:
                aux[subtarget].add(prev + (candidate,))
    return list(aux[-1])


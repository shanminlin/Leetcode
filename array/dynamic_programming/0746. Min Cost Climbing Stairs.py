#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).<br>
# 
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.<br>
# 
# Example 1:<br>
# Input: cost = [10, 15, 20]<br>
# Output: 15<br>
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.<br>
# 
# Example 2:<br>
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]<br>
# Output: 6<br>
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].<br>
# 
# Note:<br>
# cost will have a length in the range [2, 1000].<br>
# Every cost[i] will be an integer in the range [0, 999].<br>

# # Brainstorm
# 
# As we can start from index 0 or index 1 and we can climb either 1 step or 2 steps. There seem to be many possibilites.
# But recognize that the final step is either from i or i-1.

# In[ ]:


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if not cost:
            return 0
        elif len(cost) == 1:
            return cost[0]
        
        memo = {0: 0, 
                1: cost[0], 
                2: min(cost[0], cost[1]),
                3: min(cost[1], cost[0] + cost[2])}
        i = len(cost)
        return self.recurse(cost, i, memo)
    
    def recurse(self, cost, i, memo):
        if i in memo:
            return memo[i]
        
        memo[i] = min(cost[i-1] + self.recurse(cost, i-1, memo), cost[i-2] + self.recurse(cost, i-2, memo))
        return memo[i]
        


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.<br>
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].<br>
# 
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

# # Brainstorm
# 
# If we want to solve it in O(N), we need to store currently unsolved elements. If we find a larger element later, we need to pop elements until the unsolve elements.

# # Solution 1
# ##### nested loops

# In[ ]:


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        wait_days = []
        for i in range(len(T) - 1):
            days = 0
            for j in range(i+1, len(T)):
                if T[j] <= T[i]:
                    continue
                else:
                    days = j - i
                    break
            wait_days.append(days)
        
        wait_days.append(0)
        return wait_days
                


# # Solution 2
# ##### stack

# In[ ]:


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return [0]
        
        wait_days = [0] * len(T)
        
        unsolved_indices = []
        
        for i in range(len(T)):
            # Current temperature at i is used to solve previous temperature
            while unsolved_indices and T[unsolved_indices[-1]] < T[i]:
                unsolved_index = unsolved_indices.pop()
                wait_days[unsolved_index] = i - unsolved_index
                
            unsolved_indices.append(i)
        
        return wait_days


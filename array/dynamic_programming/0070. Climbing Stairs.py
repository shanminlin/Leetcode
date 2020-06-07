#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.
# 
# Example 1:
# - Input: 2
# - Output: 2
# - Explanation: 
# There are two ways to climb to the top.<br>
# 1) 1 step + 1 step<br>
# 2) 2 steps<br>
# 
# Example 2:
# - Input: 3
# - Output: 3
# - Explanation: 
# There are three ways to climb to the top.<br>
# 1) 1 step + 1 step + 1 step<br>
# 2) 1 step + 2 steps<br>
# 3) 2 steps + 1 step<br>
# 
# 
# brainstorming:
# first let's start with simple cases,
# when N is 1, the ways to reach to the top is [1], where the number inside is the steps that we take.
# when N is 2, the ways to reach to the top is: [1, 1], [2]
# when N is 3, the ways to reach to the top is: [1, 1, 1], [1, 2], [2, 1]. If you look at the part from step 1 to step 3,
# it is actually a staircase with 2 steps, If you ask yourself how to go from step 1 to step 3, that's actually the problem
# that we have solved before when N is 2.
# 
# when I want to reach step 4, the total number of ways to reach step 4 is the total number of ways we can reach step 3,
# (we are left with climb 1 step, that does not change the number of ways), plus the total number of ways we can reach step 2,
# then we add 2 to them.
# 
# Let's see whether this works when we have 5 steps.
# we take the ways to reach step 4, all we have to do is just climb 1 step
# Then we take the ways to reach step 3, all we have to do is just climb 2 steps.

# # Brainstorm
# 
# When N is 3, we have to climb 1 or 2 steps from the start. When N is 4, we also climb from the start. So if we can somehow make use of previous results, we can compute the number of ways to reach N.
# 
# | n   | Number of ways| How to get it|
# | ----|:-------------:|:-------------:|
# | 0   |      0        ||
# | 1   |      1        ||  
# | 2   |      2        ||
# | 3   |      3        |1+2|
# | 4   |      5        |2+3|   
# | 5   |      8        |3+5|
# | 6   |      13       |5+8|
# 
# To get the number of ways for each n, sum the number of ways for n-1 and n-2.
# - edge case when n is 0, 1 or 2, which does not satisfy the above relation.
# - Build a list, index is n, fill the list using n = list[n-1] + list[n-2]
# - Time O(N), space O(N) as we are building a list to store results from 0 to N.
# 
# Recursion
# - Time O(2^N) as we have 2^N number of nodes in our recursion tree. Space O(N) as the recursion depth can go upto N.
# 
# Recursion with memoization
# - Time O(N), Space O(N)

# # Solution 1
# ##### Tabulation

# In[ ]:


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        
        num_of_ways = [None] * (n + 1)
        num_of_ways[0] = 0
        num_of_ways[1] = 1
        num_of_ways[2] = 2
        
        for i in range(3, n+1):
            num_of_ways[i] = num_of_ways[i-1] + num_of_ways[i-2]
            
        return num_of_ways[n]


# # Solution 2
# ##### Recursion without memoization

# In[ ]:


class Solution:
    def climbStairs(self, n: int) -> int:
    
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# # Solution 3
# ##### Recursion with memoization (array)

# In[ ]:


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        
        memo = [-1] * (n+1)
        memo[1] = 1
        memo[2] = 2
        return self.recurse(n, memo)
    
    def recurse(self, n, memo):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        elif memo[n] != -1:
            return memo[n]
        
        
        memo[n] = self.recurse(n-1, memo) + self.recurse(n-2, memo)
        
        return memo[n]


# # Solution 4
# ##### Recursion with memoization (dictionary)

# In[ ]:


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        
        memo = {1: 1, 2: 2}
        return self.recurse(n, memo)
    
    def recurse(self, n, memo):
        if n == 1 or n == 2:
            return memo[n]
        
        elif n in memo:
            return memo[n]
        
        memo[n] = self.recurse(n-1, memo) + self.recurse(n-2, memo)
        return memo[n]


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:<br>
# 
# [<br>
#   "((()))",<br>
#   "(()())",<br>
#   "(())()",<br>
#   "()(())",<br>
#   "()()()"<br>
# ]

# # Brainstorm
# 
# We are actually trying to find all possible combinations of 2n brackets, each with 2 choices only.
# The challenge is that we have to make sure the brackets generated are balanced. What does this mean?
# How can we check this? 

# In[ ]:


class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
        
        all_parentheses = []
        curr_combination = ''
        self.helper(all_parentheses, curr_combination, n, 0, 0, 0)
        return all_parentheses
    
    def helper(self, all_parentheses, curr_combination, n, i, nopen, nclose):
        if i == 2*n:
            all_parentheses.append(curr_combination)
            return 
    
        # If the number of open brackets so far > that of close brackets
        if i != 0 and nopen > nclose:
            self.helper(all_parentheses, curr_combination+')', n, i+1, nopen, nclose+1)
        
        # Use 'if' not 'elif' as this is at the same level as the above in the recursion tree
        if nopen < n:
            self.helper(all_parentheses, curr_combination+'(', n, i+1, nopen+1, nclose)


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# 
# Solution:
# 1. Clarify the question:
# Repeat the question: So we are given a linked list and a value x, and we need to shift the elements in the linked list
# such that the elements less that x come before the elements greater or equal to x.
# Clarify assumptions: -
#                      - Is it a singly or doubly linked list? (We will assume singly.).
# 
# 2. Inputs and outputs:
# 
# Input: "{[]}"<br>
# Output: true<br>
# 
# Input: "()"<br>
# Output: true<br>
# 
# Input: "()[]{}"<br>
# Output: true<br>
# 
# Input: "(]"<br>
# Output: false<br>
# 
# Input: "([)]"<br>
# Output: false<br>
# 

# # Brainstorm
# 
# Matching brackets:
# - stack to handle matches

# # Solution
# ##### Stack

# In[ ]:


class Solution:
    def isValid(self, s):
        if not s:
            return True
        
        # Use a dictionary so that when we see a close bracket,
        # we quickly know what its matching open bracket is,
        # and compare with latest seen open bracket
        close_brackets = {')': '(', ']': '[', '}': '{'}
        seen = []
        
        for char in s:
            if char not in close_brackets:
                # char is open bracket
                seen.append(char)
                
            else: # char is close bracket
                if not seen or close_brackets[char] != seen[-1]:
                    return False
                else:
                    seen.pop()
        
        if seen: # We have unmatched open brackets
            return False
        return True


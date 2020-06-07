#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
# We repeatedly make duplicate removals on S until we no longer can.<br>
# 
# Return the final string after all such duplicate removals have been made.<br>
# 
# It is guaranteed the answer is unique.
# 
# Example 1:
# 
# Input: "abbaca"<br>
# Output: "ca"<br>
# 
# Explanation: <br>
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
#  
# 
# Note:
# 
# 1 <= S.length <= 20000<br>
# S consists only of English lowercase letters.
# 

# # Brainstorm
# 
# Be careful when the stack is empty after popping.

# # Solution

# In[ ]:


class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        if not S or len(S) == 1:
            return S
        
        stack = []
        
        for char in S:
            if stack == [] or char != stack[-1]:
                stack.append(char)
            
            else:
                stack.pop()
                
        return ''.join(stack) # how about ''.join(char for char in stack)? it also works though.


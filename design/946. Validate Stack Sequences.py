#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.
# 
# Example 1:<br>
# 
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]<br>
# Output: true<br>
# Explanation: We might do the following sequence:<br>
# push(1), push(2), push(3), push(4), pop() -> 4,<br>
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1<br>
# 
# Example 2:<br>
# 
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]<br>
# Output: false<br>
# Explanation: 1 cannot be popped before 2.<br>
#  
# 
# Note:
# 
# 0 <= pushed.length == popped.length <= 1000<br>
# 0 <= pushed[i], popped[i] < 1000<br>
# pushed is a permutation of popped.<br>
# pushed and popped have distinct values.<br>

# # Brainstorm
# 
# Use the pushed stack to simulate the formation of the stack. As we perform the push to a new stack, we pop when the top of the new stack is the same as the popped stack. If they match, we remove that item from both the popped array and the new stack. After we pushed all elements, the popped array should be empty if the sequences are valid.
# - Time O(N)
# - space O(N)

# # Solution

# In[ ]:


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [] # To push elements in pushed
        i = 0 # To check elements in popped
        for item in pushed:
            stack.append(item)
            while stack:
                if stack[-1] == popped[i]:
                    stack.pop()
                    i += 1
                else:
                    break
        
        # If stack is empty, that means all elements match the sequence of popped
        return stack == []


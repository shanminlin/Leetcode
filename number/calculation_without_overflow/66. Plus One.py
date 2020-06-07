#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# 
# Example 1:<br>
# 
# Input: [1,2,3]<br>
# Output: [1,2,4]<br>
# Explanation: The array represents the integer 123.<br>
# 
# Example 2:
# 
# Input: [4,3,2,1]<br>
# Output: [4,3,2,2]<br>
# Explanation: The array represents the integer 4321.

# # Solution
# ##### Avoiding overflow

# In[ ]:


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            return digits[:-1] + [digits[-1] + 1]
        
        # If last digit is 9, we need to compute carry
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            curr_sum = digits[i] + carry
            if curr_sum == 10:
                digits[i] = 0
            else:
                digits[i] = curr_sum
                return digits
            
            if curr_sum == 10 and i == 0:
                digits[0] = 0
                return [1] + digits


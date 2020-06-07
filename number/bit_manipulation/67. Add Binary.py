#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:<br>
# 
# Input: a = "11", b = "1"<br>
# Output: "100"<br>
# 
# Example 2:<br>
# 
# Input: a = "1010", b = "1011"<br>
# Output: "10101"<br>
#  
# 
# Constraints:
# 
# Each string consists only of '0' or '1' characters.<br>
# 1 <= a.length, b.length <= 10^4<br>
# Each string is either "0" or doesn't contain any leading zero.

# In[ ]:


class Solution:
    def addBinary(self, a, b):
        # Convert string to binary 
        num1 = int(a, 2)
        num2 = int(b, 2)
        
        # Compute digit and carry
        # No need to do a loop as we 
        # can use bit operation to compute in one go
        # without integer overflow
        while num2:
            digits = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = digits
            num2 = carry
            
        # Convert result to string
        return bin(num1)[2:]


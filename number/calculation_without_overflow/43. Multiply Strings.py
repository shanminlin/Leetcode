#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# 
# Example 1:<br>
# 
# Input: num1 = "2", num2 = "3"<br>
# Output: "6"<br>
# 
# Example 2:<br>
# 
# Input: num1 = "123", num2 = "456"<br>
# Output: "56088"<br>
# 
# Note:
# 
# The length of both num1 and num2 is < 110.<br>
# Both num1 and num2 contain only digits 0-9.<br>
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.<br>
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# In[ ]:


class Solution:
    def multiply(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        power = 0
        total_sum = 0
        
        # From least significant digit 
        for i in range(len1 - 1, -1, -1):
            power1 = len1 - 1 - i
            curr_sum = 0
            for j in range(len2 - 1, -1, -1):
                power2 = len2 - 1 - j
                curr_sum += int(num1[i]) * (10**power1) * int(num2[j]) * (10**power2)
            total_sum += curr_sum
        return str(total_sum)


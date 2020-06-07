#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:<br>
# 
# Input: 123<br>
# Output: 321<br>
# 
# Example 2:
# 
# Input: -123<br>
# Output: -321<br>
# 
# Example 3:
# 
# Input: 120<br>
# Output: 21<br>
# 
# Note:<br>
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# In[ ]:



import sys

class Solution:
    def reverse(self, x: int) -> int:
        """
        x_pos = abs(x)
            
        reverted_number = 0
        while x_pos > 0:
            reverted_number = reverted_number * 10 + x_pos % 10
            x_pos //= 10
        
        if reverted_number > 2 ** 31:
            return 0
        if x >= 0:
            return reverted_number
        else:
            return reverted_number * (-1)
        """
        # improve solution
        max_int = sys.maxsize
        min_int = -sys.maxsize - 1
        
        reverted_number = 0
        while x != 0:
            
            if reverted_number > 2**31-1 or reverted_number < -2**31:
            #if reverted_number > max_int or reverted_number < min_int:
                return 0
            
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
            

        return reverted_number


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Implement atoi which converts a string to an integer.
# 
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# 
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned.
# 
# Note:
# 
# Only the space character ' ' is considered as whitespace character.<br>
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# 
# Example 1:
# 
# Input: "42"<br>
# Output: 42<br>
# 
# Example 2:
# 
# Input: "   -42"<br>
# Output: -42<br>
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# 
# Example 3:
# 
# Input: "4193 with words"<br>
# Output: 4193<br>
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# 
# Example 4:
# 
# Input: "words and 987"<br>
# Output: 0<br>
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.
#              
# Example 5:
# 
# Input: "-91283472332"<br>
# Output: -2147483648<br>
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

# In[13]:


class Solution:
    def myAtoi(self, str):
        # Edge cases
        if str is None or str == '':
            return 0
            
        # Remove leading while spaces
        s = str.lstrip()
        if s == '':
            return 0

        # Get the sign
        sign = 1
        if s[0] == '+':
            sign *= 1
        elif s[0] == '-':
            sign *= -1
        
        # Convert digit to number
        number = 0
        base = 10
        i = 0
        # For cases like '+1' or '-1'
        if s[0] == '-' or s[0] == '+':
            i = 1
        while i < len(s) and s[i].isdigit():
            number = number * base + ord(s[i]) - ord('0')
            i += 1

        # Handle overflow and sign
        MAX = 2**31 - 1
        MIN = -2**31
        number = number * sign
        if number > MAX:
            return MAX
        elif number < MIN:
            return MIN
        else:
            return number


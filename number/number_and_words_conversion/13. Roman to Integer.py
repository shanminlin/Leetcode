#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# 
# |Symbol| Value|
# | ------------- |:-------------:| 
# |I   |  1|
# |V   |  5|
# |X   |  10|
# |L   |  50|
# |C   |  100|
# |D   |  500|
# |M   |  1000|
# 
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# 
# I can be placed before V (5) and X (10) to make 4 and 9.<br>
# X can be placed before L (50) and C (100) to make 40 and 90. <br>
# C can be placed before D (500) and M (1000) to make 400 and 900.<br>
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
# 
# Example 1:<br>
# 
# Input: "III"<br>
# Output: 3<br>
# 
# Example 2:<br>
# 
# Input: "IV"<br>
# Output: 4<br>
# 
# Example 3:<br>
# 
# Input: "IX"<br>
# Output: 9<br>
# 
# Example 4:
# 
# Input: "LVIII"<br>
# Output: 58<br>
# Explanation: L = 50, V= 5, III = 3.<br>
# 
# Example 5:
# 
# Input: "MCMXCIV"<br>
# Output: 1994<br>
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# # Solution 1

# In[ ]:


class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbols = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
        
        specials = {'I': set(['V', 'X']),
                  'X': set(['L', 'C']),
                  'C': set(['D', 'M'])}
        
        number = 0
        for i in range(len(s)):
            if s[i] in specials and i < len(s) - 1:
                if s[i+1] in specials[s[i]]:
                    number -= symbols[s[i]]
                else:
                    number += symbols[s[i]]
            else:
                number += symbols[s[i]]
        return number


# # Solution 2

# In[ ]:


class Solution:
    def romanToInt(self, s):
        
        symbols = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
        
        number = 0
        for i in range(len(s)):
            # Observe that the special cases are when 
            # the current number is smaller than the next one
            if i < len(s) - 1 and symbols[s[i]] < symbols[s[i+1]]:
                number -= symbols[s[i]]
            else:
                number += symbols[s[i]]
        return number


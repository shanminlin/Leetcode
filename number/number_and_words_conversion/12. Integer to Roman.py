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
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.<br>
# 
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:<br>
# 
# I can be placed before V (5) and X (10) to make 4 and 9.<br>
# X can be placed before L (50) and C (100) to make 40 and 90.<br>
# C can be placed before D (500) and M (1000) to make 400 and 900.<br>
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.<br>
# 
# Example 1:<br>
# 
# Input: 3<br>
# Output: "III"<br>
# 
# Example 2:
# 
# Input: 4<br>
# Output: "IV"<br>
# 
# Example 3:
# 
# Input: 9<br>
# Output: "IX"<br>
# 
# Example 4:
# 
# Input: 58<br>
# Output: "LVIII"<br>
# Explanation: L = 50, V = 5, III = 3.<br>
# 
# Example 5:
# 
# Input: 1994<br>
# Output: "MCMXCIV"<br>
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# In[ ]:


class Solution:
    def intToRoman(self, num: int) -> str:
        
        # Get digits 
        k = num // 1000
        h = num % 1000 // 100
        t = num % 100 // 10
        ones = num % 10
        
        roman = ''
        if k:
            roman += 'M' * k
        
        if h:
            if h <= 3:
                roman += 'C' * h
            elif h == 4:
                roman += 'CD'
            elif 5 <= h <= 8:
                roman += 'D' + 'C' * (h - 5)
            else:
                roman += 'CM'
        
        if t:
            if t <= 3:
                roman += 'X' * t
            elif t == 4:
                roman += 'XL'
            elif 5 <= t <= 8:
                roman += 'L' + 'X' * (t - 5)
            else:
                roman += 'XC'
        
        if ones:
            if ones <= 3:
                roman += 'I' * ones
            elif ones == 4:
                roman += 'IV'
            elif 5 <= ones <= 8:
                roman += 'V' + 'I' * (ones - 5)
            else:
                roman += 'IX'
                
        return roman


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of characters, compress it in-place.
# 
# The length after compression must always be smaller than or equal to the original array.
# 
# Every element of the array should be a character (not int) of length 1.
# 
# After you are done modifying the input array in-place, return the new length of the array.
# 
#  
# Follow up:
# Could you solve it using only O(1) extra space?

# # Brainstorm
# 
# Prone to off-by-one error

# In[ ]:


class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = 0
        fill_index = 0  
        while i < len(chars):
            start_char = chars[i]
            count = 1
            while i + 1 < len(chars) and chars[i+1] == chars[i]:
                i += 1
                count += 1
                
            if count > 1:
                chars[fill_index] = start_char
                for digit in str(count):
                    fill_index += 1
                    chars[fill_index] = digit
            else:
                chars[fill_index] = start_char
            
            fill_index += 1
            i += 1
        return len(chars[:fill_index])


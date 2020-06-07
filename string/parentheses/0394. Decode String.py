#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
# 
# Examples:
# 
# s = "3[a]2[bc]", return "aaabcbc".<br>
# s = "3[a2[c]]", return "accaccacc".<br>
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

# # Brainstorm
# 
# We see brackets, so a stack is a potential data structure to help us reduce iterations.
# 
# Also notice, besides brackets, we deal with numbers (eg. 2, 20, 200) and letters (eg. a, ab, abc). So if the number is 100, we need to add [100] to the stack, not [1, 0, 0]
# 
# Then have to try several representative examples that cover enough cases:
# - 2[a2[b]] where we have letter followed by digits. Because of cases like this, it is not trivial to find the patten.

# In[ ]:


class Solution:
    def decodeString(self, s: str) -> str:
        
        num = []
        substring = []
        chars = None
        decoded_s = None
        
        for i, char in enumerate(s):
            if char.isdigit() or char == '[':
                num.append(char)
            elif char.isalpha():
                j = i + 1
                chars = char
                while j < len(s) and s[j].isalpha():
                    chars += s[j]
                    j += 1
                substring.append(chars)
                
            else:
                num.pop()
                n = num.pop()
      
                substring[-1] *= int(n)
                if decoded_s:
                    decoded_s += substring
                else:
                    decoded_s = substring
                substring.pop()
        
        return decoded_s


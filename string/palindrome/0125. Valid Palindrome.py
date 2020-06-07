#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.<br>
# 
# Note: For the purpose of this problem, we define empty string as valid palindrome.<br>
# 
# Example 1:<br>
# 
# Input: "A man, a plan, a canal: Panama"<br>
# Output: true<br>
# 
# Example 2:<br>
# 
# Input: "race a car"<br>
# Output: false<br>

# # Brainstorm
# 
# Basics:<br>
# Check whether a character in string is a letter or a number:
# - char.isalnum()
# 
# Convert string to lower letters:
# - string.lower()
# 
# 
# Solution:
# Using two pointers, from each end of the string, moving to the middle.
# - Time: O(N) as we iterate through the string once, space O(1)
# 
# Using regular expressions
# - Time: O(N), space O(N) as we store two new strings: one is the cleaned string, the other is the reverse of the cleaned string.

# # Solution 1
# ##### Pointers

# In[1]:


class Solution:
    def isPalindrome(self, s):
        
        if not s:
            return True
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
                
            elif not s[right].isalnum():
                right -= 1
            
            
            elif s[left].lower() != s[right].lower():
                return False
            
            else:
                left += 1
                right -= 1
            
        return True


# # Solution 2
# ##### Regular expression

# In[2]:


import re
class Solution:
    def isPalindrome(self, s):
        
        if not s:
            return True
        
        s1 = re.sub('[^a-zA-Z0-9]+', '', s).lower()
        
        return s1 == s1[::-1]


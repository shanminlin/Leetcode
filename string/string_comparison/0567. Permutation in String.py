#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# 
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
# 
#  
# 
# Example 1:<br>
# Input: s1 = "ab" s2 = "eidbaooo"<br>
# Output: True<br>
# Explanation: s2 contains one permutation of s1 ("ba").<br>
# 
# Example 2:<br>
# Input:s1= "ab" s2 = "eidboaoo"<br>
# Output: False<br>

# # Brainstorm
# 
# There are several complications in this problem:
# - duplicate letters in s1
# - permutations
# 
# 
# We see permutation, so a hash table may be helpful to reduce iterations as the order of letters is not important and we need to quickly search for the presence of a letter.
# 
# - Store the characters in s1 into a set. eg. 'ab' to set([a, b])
# - Iterate s2, eg. 'ebcbaooooa'
#       - if a letter in s2 exists in s1, check for the substring starting from that letter. we find b at index 1 in s2. check for substring with length 2 --'bc', which is not the same as 'ab', then go on to the next index in s2.
# - Time O(N) where N is the length of s2. Space O(kM) where M is the length of s1, k is the set, and multiple substrings created for comparision.

# # Solution
# 
# We see permutations, so a hash table could be helpful to reduce iterations as we don't care about the order and need quick 

# In[ ]:





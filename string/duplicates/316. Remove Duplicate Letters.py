#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
# 
# Example 1:<br>
# 
# Input: "bcabc"<br>
# Output: "abc"<br>
# 
# Example 2:<br>
# 
# Input: "cbacdcbc"<br>
# Output: "acdb"<br>
# 
# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

# # Brainstorm
# 
# Removing duplicates is straightforward if O(N) time and O(N) space --- Use a set to contain nonduplicate letters and convert to string.
# 
# How to find the smallest lexicograpical order? 
# Use sort does not work as the result should not only be the smallest but also in the order of the characters in the given string. 

# In[ ]:





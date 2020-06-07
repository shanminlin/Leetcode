#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Implement strStr().<br>
# 
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.<br>
# 
# Example 1:<br>
# 
# Input: haystack = "hello", needle = "ll"<br>
# Output: 2<br>
# 
# Example 2:<br>
# 
# Input: haystack = "aaaaa", needle = "bba"<br>
# Output: -1<br>
# 
# Clarification:<br>
# 
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# # Brainstorm
# Compare character by character
# - Time O(N*M), space O(1)
# - since it compares character by character instead of substring, so operations of comparison is len(needle) times more.
# 
# Compare substring
# - Time O(N), space O(N*M)
# 
# KMP algorithm
# - Time O(N+M), space O(M)

# In[40]:


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if not haystack:
            return -1        

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                j = 1
                found = True
                while j < len(needle):
                    if i+j >= len(haystack) or haystack[i+j] != needle[j]:
                        found = False
                        break
                    else:
                        j += 1

                if found == False:
                    continue
                else:
                    return i

        return -1


# # Solution 2
# 

# In[ ]:


def strStr(self, haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack)-len(needle)+1):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j == len(needle)-1:
                return i
    return -1


# # Solution 3
# ##### string slicing

# In[ ]:


class Solution(object):
def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


# In[ ]:





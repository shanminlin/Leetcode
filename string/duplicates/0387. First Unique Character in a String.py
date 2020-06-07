#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.<br>
# 
# Examples:<br>
# 
# s = "leetcode"<br>
# return 0.<br>
# 
# s = "loveleetcode",<br>
# return 2.<br>
# 
# Note: You may assume the string contain only lowercase letters.

# # Brainstorm
# 
# If using indices and constant space, time is O(N^2).
# To reduce time, think of keeping track of the elements using a data structure. 
# - non-repeating, a set or dictionary seems suitable.
# - Time O(N), space O(N)

# # Solution 1
# ##### two pass over s 

# In[ ]:


from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1
        
        if len(s) == 1:
            return 0
        
        # Dictionary key: letters in s
        # value: count of each letter
        count = Counter(s)
        
        # Iterate the array again because dictionary does not
        # maintain order before Python 3.6
        for i, char in enumerate(s):
            # First unique character, return its index
            if count[char] == 1:
                return i
        return -1


# # Solution 2
# ##### one pass over s, one pass over d 

# In[ ]:


class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1
        
        if len(s) == 1:
            return 0
        
        # Dictionary key: letters in s
        # value: index of each unique letter, None for duplicates
        unique_letter = {}
        for i, char in enumerate(s):
            if char not in unique_letter:
                unique_letter[char] = i
            else:
                unique_letter[char] = None
                
        min_index = float('inf')
        for letter, index in unique_letter.items():
            if index is not None:
                min_index = min(min_index, index)

        return min_index if min_index != float('inf') else -1


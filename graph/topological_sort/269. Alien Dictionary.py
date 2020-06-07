#!/usr/bin/env python
# coding: utf-8

# # 269. Alien Dictionary
# 
# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
# 
# Example 1:<br>
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]<br>
# Output: "wertf"<br>
# 
# Example 2:<br>
# Input:
# [
#   "z",
#   "x"
# ]
# Output: "zx"<br>
# 
# Example 3:<br>
# Input:
# [
#   "z",
#   "x",
#   "z"
# ] 
# Output: "" 
# 
# Explanation: The order is invalid, so return "".
# 
# Note:
# - You may assume all letters are in lowercase.
# - You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# - If the order is invalid, return an empty string.
# - There may be multiple valid order of letters, return any one of them is fine.

# 

# In[10]:


# build a dictionary for each letter in the words
words = ["wrt", "wrf", "er", "ett", "rftt"]
chars = set(''.join(words))
chars_dict = {char:0 for char in chars}
chars_list = [char for char in chars]


# In[11]:


print(chars_list)


# In[ ]:





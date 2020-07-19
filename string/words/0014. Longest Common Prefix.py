#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Write a function to find the longest common prefix string amongst an array of strings.<br>
# 
# If there is no common prefix, return an empty string "".<br>
# 
# Example 1:<br>
# 
# Input: ["flower","flow","flight"]<br>
# Output: "fl"<br>
# 
# Example 2:
# 
# Input: ["dog","racecar","car"]<br>
# Output: ""<br>
# Explanation: There is no common prefix among the input strings.<br>
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.

# # Brainstorm
# 
# string contecanation
# - Time O(mN) where m is the length of the first string, space O(M) where M is the length of the common prefix, the longest M can be the shortest string. 
# - be careful of the case when strs are ['', '', '']

# # Solution

# In[ ]:


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        pre = ""
        first_str = strs[0]
        
        for i in range(len(first_str)):
            add_i_to_pre = True
            for s in strs[1:]:
                if i >= len(s) or s[i] != first_str[i]:
                    add_i_to_pre = False
                    break
                else:
                    continue
            
            if add_i_to_pre == False:
                return pre
            else:
                pre += first_str[i]
        
        return pre


# Simplify:



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        
        first_str = strs[0]
        
        for i in range(len(first_str)):

            for s in strs[1:]:
                if i >= len(s) or s[i] != first_str[i]:
                    return first_str[:i]
                
        return first_str


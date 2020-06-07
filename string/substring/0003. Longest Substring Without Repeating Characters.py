#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string, find the length of the longest substring without repeating characters.
# 
# Example 1:
# 
# Input: "abcabcbb"<br>
# Output: 3 <br>
# Explanation: The answer is "abc", with the length of 3. <br>
# 
# Example 2:
# 
# Input: "bbbbb"<br>
# Output: 1<br>
# Explanation: The answer is "b", with the length of 1.<br>
# 
# Example 3:
# 
# Input: "pwwkew"<br>
# Output: 3<br>
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# # Brainstorm
# 
# Be careful of edge cases like '' and ' '.
# 
# Use a set to record seen letters every time we iterate i
# - for each i, initiate a new set, iterate s again from i+1 until the end of the string
# - fill set until letter is already seen
# - length of nonduplicated substring is the length of the set
# - move to the next i
# - Time O(N^2), space O(Nm) where m is the length of each set.
# 
# Use a dictionary to record seen letters and their position, so we can skip some i
# - for each i, initiate a new dict, iterate s again from i+1 until the end of the string
# - fill dictionary with value and index
# - If a letter is already seen at a previous position, start next i from that position + 1 to skip the seen letter.
# - Same time and space complexity as above
# 
# Can we use only one dictionary? If so, we cannot use the length of the dictionary to calculate each nonduplicated substring. In the previous dictionary solution, we already know the start of the substring. We can use that to calculate the nonduplicated substring.

# # Solution 1
# ##### set

# In[2]:


class Solution:
    def lengthOfLongestSubstring(self, s):
        
        max_length = 0
        for i in range(len(s)): # it may be tempting to end the range as len(s)-1, but think about the case when len(s) == 1
            seen = set([s[i]])
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    
            length = len(seen)
            max_length = max(max_length, length)
            
        return max_length
                    


# # Solution 2
# ##### dictionary

# In[ ]:


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        max_length = 0
        for i in range(start, len(s)):
            seen_at = {s[i]: i}
            for j in range(i+1, len(s)):
                if s[j] in seen_at:
                    start = seen_at[s[j]] + 1
                    break
                else:
                    seen_at[s[j]] = j
            length = len(seen_at)
            max_length = max(max_length, length)
        
        return max_length


# # Solution 3
# ##### Use only 1 dictionary

# In[ ]:


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        max_length = 0
        seen_at = {}
        
        for i in range(len(s)):
            if s[i] not in seen_at or (s[i] in seen_at and seen_at[s[i]] < start):
                length = i - start + 1
                max_length = max(max_length, length)
                seen_at[s[i]] = i
            else:
                start = seen_at[s[i]] + 1
                # length = i - start
                # max_length = max(max_length, length)
                seen_at[s[i]] = i
        
        return max_length


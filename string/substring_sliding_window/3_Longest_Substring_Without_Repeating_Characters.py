#!/usr/bin/env python
# coding: utf-8

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
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
- sliding window

"""

# # Solution 1
# ##### set


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
# ##### sliding window: Use only 1 dictionary

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s):
        
        # Initialize counter to store characters in sliding window
        window = Counter()
        
        # Initialize variable to store result
        max_length = 0
        
        # Initialize pointers for sliding window
        left = 0
        right = 0
        
        while right < len(s):
            # Update counter seen
            char = s[right]
            window[char] += 1
            
            if window[char] == 1:
                # Update result
                max_length = max(max_length, right - left + 1)
                
            else: # seen[char] > 1, a duplicate appears
                while window[char] > 1:
                    # slide left pointer until the same character removed from sliding window
                    window[s[left]] -= 1
                    left += 1
            
            right += 1
        return max_length


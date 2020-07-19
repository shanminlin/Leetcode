#!/usr/bin/env python
# coding: utf-8

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"

Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
# Brute force solution: O(N^3)
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        left = -1
        right = len(s) 
        min_length = len(s) + 1
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                needs = Counter(t)
                substring = s[i:j+1]
                window = Counter(substring)
                if self.is_valid(window, needs):
                    if len(substring) < min_length:
                        left = i
                        right = j
                        min_length = len(substring)
                    break
                    
        if min_length < len(s) + 1:
            return s[left: right+1]
        else:
            return ''
    
    def is_valid(self, window, needs):
        for key, value in window.items():
            if key in needs:
                needs[key] -= value
        
        for value in needs.values():
            if value > 0:
                return False
        
        return True
    
    
# Sliding window: O(N+M)
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if not s or not t:
            return ''
        
        # Count frequencies of characters in t
        needs = Counter(t)
        
        # Initiate variables to store result
        min_length = float('inf')
        final_left = 0
        final_right = 0
        
        # Initiate variables to check whether substring is valid
        window = Counter()
        formed = 0
        required = len(needs)
        
        left = 0
        for right, char in enumerate(s):
            window[char] += 1
            
            if window[char] == needs[char]:
                formed += 1
            
            # Found valid substring, slide left pointer to shrink
            while formed == required and left <= right: 
                # Update result
                curr_length = right - left + 1
                if curr_length < min_length:
                    min_length = curr_length
                    final_left = left
                    final_right = right
                    
                # Modify window dictionary as window shrinked
                char = s[left]
                window[char] -= 1
                
                # If removed desired characters, substring not valid
                if window[char] < needs[char]:
                    formed -= 1
                
                left += 1
        
        return '' if min_length == float('inf') else s[final_left: final_right+1]











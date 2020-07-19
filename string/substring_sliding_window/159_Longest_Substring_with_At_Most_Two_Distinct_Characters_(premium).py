#!/usr/bin/env python
# coding: utf-8

"""
Given a string s , find the length of the longest substring t that contains at most 2 distinct characters.
Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

"""
from collections import Counter

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        
        # Initialize variable to store result
        max_length = 0
        
        # initialize sliding window parameters
        window = Counter()
        left = 0
        right = 0
        
        while right < len(s):
            char = s[right]
            window[char] += 1
            
            if len(window) <= 2:
                max_length = max(max_length, right-left+1)
                
            else: # len(window) > 2
                # move left pointer until len(window) == 2
                while len(window) > 2:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
            
            right += 1
        
        return max_length



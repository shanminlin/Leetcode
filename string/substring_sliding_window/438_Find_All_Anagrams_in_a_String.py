# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:28:32 2020

@author: SS

Problem

Given a string s and a non-empty string p, find all the start indices of p’s anagrams in s.
Strings consist of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
Example 1:
Input: s: "cbaebabacd" p: "abc"
Output: [0, 6]
"""
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        # Count frequencies of characters in p
        needs = Counter(p)
        
        # Initialize list to store result
        result = []
        
        # Initialize sliding window
        window = Counter()
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            
            if right - left + 1 == len(p): 
                if window == needs:
                    result.append(left)
            
                # Move sliding window
                window[s[left]] -= 1
                
                # Have to delete key if value is 0
                # if not, window will have extra keys compared to needs
                if window[s[left]] == 0:
                    del window[s[left]]
                    
                left += 1

        return result
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:26:25 2020

@author: SS

Problem
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string’s permutations is the substring of the second string.

Example 1:

Input: s1 = “ab” s2 = “eidbaooo”
Output: True
Explanation: s2 contains one permutation of s1 (“ba”).

"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False
        
        needs = Counter(s1)
        
        # Initialize sliding window
        window = Counter()
        left = 0
        for right in range(len(s2)):
            char = s2[right]
            window[char] += 1
            
            if right - left + 1 == len(s1):
                if window == needs:
                    return True
                
                # if not true, move window
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1       
                
        return False

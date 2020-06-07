#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# 
# Example:
# 
# Input: "23"<br>
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].<br>
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be in any order you want.

# # Brainstorm
# 
# List out all choices and build from each digit.
# - Time O(3^K * 4^M) where k + M is the total number of digits. K digits have 3 choices of letters, M digits have 4 choices of letters.
# - Space like the height of a tree, O(K + M) for the recursion stack.

# # Solution 

# In[ ]:


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        mapping = {'2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z']}
        
        all_letters = []
        self.helper(all_letters, digits, 0, '', mapping)
        return all_letters
    
    def helper(self, all_letters, digits, i, curr_combination, mapping):
        # No more letters to add to a combination
        if i >= len(digits):
            all_letters.append(curr_combination)
            return
        
        digit = digits[i]
        for letter in mapping[digit]:
            self.helper(all_letters, digits, i+1, curr_combination+letter, mapping)


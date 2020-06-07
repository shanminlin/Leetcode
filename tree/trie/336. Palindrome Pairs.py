#!/usr/bin/env python
# coding: utf-8

# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
# 
# Example 1:<br>
# Input: ["abcd","dcba","lls","s","sssll"]<br>
# Output: [[0,1],[1,0],[3,2],[2,4]]<br>
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# Example 2:<br>
# Input: ["bat","tab","cat"]<br>
# Output: [[0,1],[1,0]]<br>
# Explanation: The palindromes are ["battab","tabbat"]

# 4. Brainstorm
# - Naive solution, for each word, we go through all words in the array, check whether the concatenated string is a palindrome. The time complexity: there are O(N^2) iterations, and for each iteration, we need to check whether the string is palindrome, which takes O(k/2) where k is the length of the concatenated words. So total time complexity is O(N^2 * k)
# - To improve the algorithm, we can think in the direction that is to reduce the number of words that need to be check. 

# In[ ]:





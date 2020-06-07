#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string s, partition s such that every substring of the partition is a palindrome.<br>
# 
# Return all possible palindrome partitioning of s.<br>
# 
# Example:<br>
# Input: "aab"<br>
# Output:<br>
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

# Solution 1: Backtrack

# In[1]:


def partition(s):
    partitions = []
    backtrack(s, 0, [], partitions)
    return partitions
    
def backtrack(s, start, templist, partitions):
    if start == len(s):
        partitions.append(templist[:])
    for i in range(start, len(s)):
        current = s[start:i+1]
        if current == current[::-1]:
            templist.append(current)
            backtrack(s, i+1, templist, partitions)
            templist.pop()


# In[2]:


s = 'aab'
partition(s)


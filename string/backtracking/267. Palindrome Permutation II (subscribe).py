#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.<br>
# 
# Example 1:<br>
# 
# Input: "aabb"<br>
# Output: ["abba", "baab"]<br>
# 
# 
# Example 2:
# 
# Input: "abc"<br>
# Output: []

# In[ ]:


def generatePalindromes(self, s):
        kv = collections.Counter(s)
        mid = [k for k, v in kv.iteritems() if v%2]
        if len(mid) > 1:
            return []
        mid = '' if mid == [] else mid[0]
        half = ''.join([k * (v/2) for k, v in kv.iteritems()])
        half = [c for c in half]
        
        def backtrack(end, tmp):
            if len(tmp) == end:
                cur = ''.join(tmp)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i>0 and half[i] == half[i-1] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(half[i])
                    backtrack(end, tmp)
                    visited[i] = False
                    tmp.pop()
                    
        ans = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        return ans


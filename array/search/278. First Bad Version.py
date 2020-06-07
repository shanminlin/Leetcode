#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.<br>
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.<br>
# 
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.<br>
# 
# Example:<br>
# 
# Given n = 5, and version = 4 is the first bad version.<br>
# 
# call isBadVersion(3) -> false<br>
# call isBadVersion(5) -> true<br>
# call isBadVersion(4) -> true<br>
# 
# Then 4 is the first bad version. 

# # Brainstorm
# 
# 

# In[ ]:


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            mid_is_bad = isBadVersion(mid + 1)
            
            if mid_is_bad:
                high = mid
            else:
                low = mid + 1
            
            if low == high:
                break
                  
        return low + 1


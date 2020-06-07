#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
# 
# Since the answer may be large, return the answer modulo 10^9 + 7.
# 
#  
# 
# Example 1:<br>
# 
# Input: [3,1,2,4]<br>
# Output: 17<br>
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. <br>
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.<br>
#  
# 
# Note:
# 
# 1 <= A.length <= 30000<br>
# 1 <= A[i] <= 30000

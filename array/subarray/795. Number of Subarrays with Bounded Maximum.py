#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# We are given an array A of positive integers, and two positive integers L and R (L <= R).
# 
# Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.
# 
# Example :<br>
# Input: <br>
# A = [2, 1, 4, 3]<br>
# L = 2<br>
# R = 3<br>
# Output: 3<br>
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].<br>
# 
# Note:
# 
# L, R  and A[i] will be an integer in the range [0, 10^9].<br>
# The length of A will be in the range of [1, 50000].

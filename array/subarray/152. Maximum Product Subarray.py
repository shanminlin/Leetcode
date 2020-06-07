#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
# 
# Example 1:<br>
# 
# Input: [2,3,-2,4]<br>
# Output: 6<br>
# Explanation: [2,3] has the largest product 6.<br>
# 
# Example 2:
# 
# Input: [-2,0,-1]<br>
# Output: 0<br>
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# # Brainstorm
# 
# If we encounter a positive number, we will include that number in our potential max product subarray. What if we encounter a negative number or zero, how does that affect our possible max product subarray?

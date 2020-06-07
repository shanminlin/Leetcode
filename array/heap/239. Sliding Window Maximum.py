#!/usr/bin/env python
# coding: utf-8

# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
# 
# Example:<br>
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3 <br>
# Output: [3,3,5,5,6,7] <br>
# Explanation:<br>
# 
# | Window position | Max |
# | --- | --- | 
# | [1  3  -1] -3  5  3  6  7  | 3 | 
# | 1 [3  -1  -3] 5  3  6  7  | 3 | 
# | 1  3 [-1  -3  5] 3  6  7    | 5 | 
# | 1  3  -1 [-3  5  3] 6  7   | 5 | 
# |  1  3  -1  -3 [5  3  6] 7    | 6 | 
# |1  3  -1  -3  5 [3  6  7]  | 7 | 

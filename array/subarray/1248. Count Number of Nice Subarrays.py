#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
# 
# Return the number of nice sub-arrays.<br>
# 
#  
# 
# Example 1:<br>
# 
# Input: nums = [1,1,2,1,1], k = 3<br>
# Output: 2<br>
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].<br>
# 
# Example 2:
# 
# Input: nums = [2,4,6], k = 1<br>
# Output: 0<br>
# Explanation: There is no odd numbers in the array.<br>
# 
# Example 3:
# 
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2<br>
# Output: 16<br>
#  
# 
# Constraints:
# 
# 1 <= nums.length <= 50000<br>
# 1 <= nums[i] <= 10^5<br>
# 1 <= k <= nums.length<br>

#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of non-negative integers, you are initially positioned at the first index of the array.<br>
# 
# Each element in the array represents your maximum jump length at that position.<br>
# 
# Determine if you are able to reach the last index.<br>
# 
#  
# 
# Example 1:<br>
# 
# Input: nums = [2,3,1,1,4]<br>
# Output: true<br>
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.<br>
# 
# Example 2:<br>
# 
# Input: nums = [3,2,1,0,4]<br>
# Output: false<br>
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.<br>
#  
# 
# Constraints:
# 
# 1 <= nums.length <= 3 * 10^4<br>
# 0 <= nums[i][j] <= 10^5<br>

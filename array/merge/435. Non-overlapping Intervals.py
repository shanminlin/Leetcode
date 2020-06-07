#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# 
# 
# Example 1:<br>
# 
# Input: [[1,2],[2,3],[3,4],[1,3]]<br>
# Output: 1<br>
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.<br>
# 
# Example 2:<br>
# 
# Input: [[1,2],[1,2],[1,2]]<br>
# Output: 2<br>
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# 
# Example 3:<br>
# 
# Input: [[1,2],[2,3]]<br>
# Output: 0<br>
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
#  
# 
# Note:
# 
# You may assume the interval's end point is always bigger than its start point.<br>
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

# # Brainstorm
# 
# If two intervals overlap, remove the interval with later ending time.

#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# We are given an array asteroids of integers representing asteroids in a row.
# 
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# 
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# 
# Example 1:<br>
# Input:<br>
# asteroids = [5, 10, -5]<br>
# Output: [5, 10]<br>
# Explanation: <br>
# The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.<br>
# 
# Example 2:<br>
# Input:<br>
# asteroids = [8, -8]<br>
# Output: []<br>
# Explanation:<br>
# The 8 and -8 collide exploding each other.<br>
# 
# Example 3:<br>
# Input:<br>
# asteroids = [10, 2, -5]<br>
# Output: [10]<br>
# Explanation:<br>
# The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.<br>
# 
# Example 4:<br>
# Input:<br>
# asteroids = [-2, -1, 1, 2]<br>
# Output: [-2, -1, 1, 2]<br>
# Explanation:<br>
# The -2 and -1 are moving left, while the 1 and 2 are moving right.<br>
# Asteroids moving the same direction never meet, so no asteroids will meet each other.<br>
# 
# Note:
# 
# The length of asteroids will be at most 10000.<br>
# Each asteroid will be a non-zero integer in the range [-1000, 1000]..

# # Brainstorm
# 
# What are all the possible scenarios? The asteroid can only move left or right.<br>
# So there are only 4 possible cases:<br>
# for any two asteroids, 2 and 1 can be any non-zero integer:
# - +2, -1
# - -2, -1
# - +2, +1
# - -2, +1
# In case 1, +2, -1, the two will collide and merge. In other cases, we will keep the two numbers.
